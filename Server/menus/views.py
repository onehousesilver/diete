from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status

from .models import Food, Menu, MenuToFood
from .serializers import FoodSerializer, MenuSerializer, MenuToFoodSerializer, FoodRecommSerializer
from image_adapter import ImageIncoder

from datetime import datetime
# 음식 추천 GET /recommend/{username}

@api_view(['GET'])
@permission_classes([AllowAny])
def recommend_foods(request, username):
    # 유저 정보
    user=get_object_or_404(get_user_model(), username=username)

    # user의 메뉴를 가져오되, dummydata는 제외
    user_menus = Menu.objects.filter(userId=user.id).exclude(dateTime= "2000-01-01")
    meat = vegetable = seafood = spicy = oily = 0 

    # dummydata를 제외하여 data가 없는 상황때문에 cnt를 기본 1
    cnt = 1
    for user_menu in user_menus:
        menuId = user_menu.id
        mtfs = MenuToFood.objects.filter(menuId=menuId)
        for mtf in mtfs:
            meat += mtf.foodId.meat
            vegetable += mtf.foodId.vegetable
            seafood += mtf.foodId.seafood
            spicy += mtf.foodId.spicy
            oily += mtf.foodId.oily
            cnt += 1

    # 유저가 선호하는 식단의 지표
    prefer_user = {"meat": meat/cnt, "vegetable": vegetable/cnt, "seafood": seafood/cnt, "spicy": spicy/cnt, "oily": oily/cnt}
    print(prefer_user)

    # 사용자 선호 정도 조사
    level = [["고기",'', 0], ["야채",'',0], ["해산물",'',0], ["매콤",'',0], ["느끼함",'',0]]
    idx = 0
    for pre in prefer_user:

        if prefer_user[pre] > 2 :
            level[idx][1] = "높음"
            level[idx][2] = prefer_user[pre]
        
        elif prefer_user[pre] < 2 : 
            level[idx][1] = "낮음"
            level[idx][2] = prefer_user[pre]
        
        else:
            level[idx][1] = "평균"
            level[idx][2] = prefer_user[pre]
        
        idx += 1
    print("level")
    # print(level)

    # 2로부터 멀리 떨어진 순서대로 정렬
    level.sort(key = lambda x : -abs(2-x[2]))
    print(level)

    ###################################################
    # 1. 0.1랑 비슷한 값을 가진 음식들을 list에 담아서 보내기
    # 2. return 형식 바꾸기 (어떻게??모르겠습니다..)

    # 유저의 선호 식단
    prefer_string = user.preference
    print(prefer_string)
    foods = (Food.objects.filter(commercialFood="품목대표", meat = 0)
    | Food.objects.filter(commercialFood="품목대표", meat = 1)
    | Food.objects.filter(commercialFood="품목대표", meat = 2))
    
    # 사용자의 선호 식단 채소, 고기, 일반에 따라 가중치 ++
    prefer_weight = {"meat": 10 ,"vegetable": 10, "seafood": 10 , "spicy": 10, "oily": 10}

    if prefer_string == "채소": 
        prefer_weight["vegetable"] = 3
    elif prefer_string == "고기":
        prefer_weight["meat"] = 3

    # DB의 모든 Food에 대하여 점수 계산
    food_list = []
    for food in foods.values():
        score = 0
        # item : meat, vegetable, seafood, spicy, oily
        for item in prefer_user:
            score += abs(prefer_user[item] - food[item])**2 *prefer_weight[item]
        # print(food["foodName"] , score)
        
        food_list.append([food["id"], round(score,3)])
    # print(food_list)
    # 값에 따라 정렬
    food_list.sort(key=lambda x: float(x[1]))

    main_food_recomm = {"전체" : ("전체11",)}
    main_rec = []
    for f in range(len(food_list)):
        if f == 10:
            break

        food = Food.objects.get(id = food_list[f][0])
        foodserializer = FoodSerializer(food)
        main_rec.append(foodserializer)
    # main_food = main_food_recomm["전체"] + main_rec

    # print(main_food)


    # return Response(main_food.data)
    return HttpResponse("hi Good")
    

# 음식 상세 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def food_detail(request,foodId):
    print(foodId)
    food = get_object_or_404(Food, pk=foodId)
    print(food)
    serializer = FoodSerializer(food)
    return Response(serializer.data)



# 추가메뉴조회 GET /submenu/{foodId}
def sub_foods(request, foodId):
    imageIncoder = ImageIncoder()

    # 1. foodId가 들어간 menuToFood "menuId"를 모두 찾기
    mtfs = MenuToFood.objects.filter(foodId = foodId)
    
    menu_id_list = []
    sub_menus = {}
    for mtf in mtfs:
        menu_id_list.append(mtf.menuId)
    print(menu_id_list)
    for menuId in menu_id_list:
        mtf_menu = MenuToFood.objects.filter(menuId = menuId)
        for mtf in mtf_menu:
            # foodId랑 같다면 pass
            if mtf.foodId.id == foodId:
                pass
            else:
                if mtf.foodId.id in sub_menus:
                    sub_menus[mtf.foodId.id] += 1
                else:
                    sub_menus[mtf.foodId.id] = 1
    
    print(sub_menus)
    # 순서대로 foodId, foodName, image, 같이 먹은 횟수 
    sub_menu_list = []
    for key in sub_menus:
        tempDict = {}
        food = Food.objects.get(id = key)
        tempDict["foodId"] = key
        tempDict["foodName"] = food.foodName
        tempDict["img"] = imageIncoder.getBase64String(food.foodName).decode('utf8')
        tempDict["cnt"] = sub_menus[key]
        sub_menu_list.append(tempDict)

    # value에 따라 내림차순 정렬
    sub_menu_list.sort(key = lambda x: -x["count"])

    return JsonResponse(sub_menu_list[:10], safe=False)





# 장바구니 최종 결정
@api_view(['POST'])
@permission_classes([AllowAny])

def decision_basket(request):
    if request.method == 'POST':
        # 사용자 모델
        user = get_object_or_404(get_user_model(), username=request.user.username)
        # request에서 menu 모델에 필요한 data 생성
        # dateTime 추가
        menudata = { 
            "userId" : user.id,
            "dateTime" : request.data["dateTime"],
            "mealTime" : request.data["mealTime"]
        }
        menuserializer = MenuSerializer(data=menudata)
        if menuserializer.is_valid(raise_exception=True):
            menuserializer.save()
            # menu에서 저장될 때 생성된 id 저장 (MenuToFood를 위해서)
            menuTempId = menuserializer.data["id"]
        else:
            return Response({'error': 'menu 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
        
        basket = request.data
        # print(type(basket), basket) # dict
        menus = basket.get("menus")
        # print(type(menus), menus) # list
        # print(type(menus[0]), menus[0]) # dict
        # print(type(menus[0].get("foodId")), menus[0].get("foodId")) # int
        # print(type(menus[0].get("amount")), menus[0].get("amount"))
        for menu in menus:
            basketdata = {
                "menuId" : menuTempId,
                "foodId" : menu.get("foodId"),
                "amount" : menu.get("amount"),
            }
            mtfserializer = MenuToFoodSerializer(data=basketdata)
            if mtfserializer.is_valid(raise_exception=True):
                mtfserializer.save()
            else: # 트랜젝션 묶어놓으면 좋을듯
                return Response({'error': 'menuToFood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'create: 데이터가 생성되었습니다.'}, status=status.HTTP_201_CREATED)

# 장바구니 수정    
@api_view(['PUT'])
@permission_classes([AllowAny])
def update_basket(request, menuId):
    if request.method == 'PUT':
        # 기존 MenuToFood에 있는 menuId인 data 삭제
        menuList = get_list_or_404(MenuToFood, menuId=menuId)
        for menu in menuList:
            menu.delete()

        basket = request.data
        menus = basket.get("menus")
        print(menus)

        # request data에 있는 값들을 다시 MenuToFood에 DB 저장
        for menu in menus:
            basketdata = {
                "menuId" : menuId,
                "foodId" : menu.get("foodId"),
                "amount" : menu.get("amount"),
            }
            mtfserializer = MenuToFoodSerializer(data=basketdata)
            if mtfserializer.is_valid(raise_exception=True):
                mtfserializer.save()
            else: # 트랜젝션 묶어놓으면 좋을듯
                return Response({'error': 'menuToFood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
            
        return Response({'update: 데이터가 업데이트되었습니다.'}, status=status.HTTP_200_OK)

# 추천알고리즘 2단계 
