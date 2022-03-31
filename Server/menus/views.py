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

from datetime import datetime
# 음식 추천 GET /recommend/{username}

@api_view(['GET'])
@permission_classes([AllowAny])
def recommend_foods(request,username):
    # 1. 유저의 이전 식단기록(음식기록) 가져오기 [나린]
    menus = getUserMenus(username)

    # 1-2. 유저의 선호 식단 받아오기 (jwt로 받기 또는 db에서 찾아오기)
    # prefer_string = getPreferString(username)
    
    # 2. 유저의 선호 태그들을 찾기 [기호]
    prefer_user = getUserPrefer(menus)

    # 3. 모든 DB의 음식들에 대하여 점수 계산 [수용, 가은]

    # prefer_user = {"meat": 1.6,"vegetable": 0.3, "seafood": 0.7 , "spicy": 1.6, "oily": 1.5}
    prefer_string = "채소" # 더미 데이터
    
    food_list = getFoodRecomm(prefer_user, prefer_string)
    
    return Response(food_list[:30], status=status.HTTP_200_OK)

def getUserMenus(username):
    result = {}
    
    user=get_object_or_404(get_user_model(), username=username)
    user_menus = Menu.objects.filter(userId=user.id)
    menuserializer = MenuSerializer(user_menus, read_only=True, many=True)
    for menu in menuserializer.data:
        result[menu["dateTime"]] = list()
        mtfs = MenuToFood.objects.filter(menuId=menu["id"])
        mtfserializers = MenuToFoodSerializer(mtfs, read_only=True, many= True)
        for mtfs in mtfserializers.data:
            food = get_object_or_404(Food, id = mtfs["foodId"])
            eat_food = {}
            eat_food["foodName"] = food.foodName
            eat_food["foodCategory"] = food.foodCategory
            eat_food["foodDetailCategory"] = food.foodDetailCategory
            eat_food["servingSize"] = food.servingSize
            eat_food["foodKcal"] = food.foodKcal
            eat_food["sugar"] = food.sugar
            eat_food["carbohydrate"] = food.carbohydrate
            eat_food["protein"] = food.protein
            eat_food["fat"] = food.fat
            eat_food["cholesterol"] = food.carbohydrate
            eat_food["fattyAcid"] = food.fattyAcid
            eat_food["spicy"] = food.spicy
            eat_food["meat"] = food.meat
            eat_food["vegetable"] = food.vegetable
            eat_food["seafood"] = food.seafood
            eat_food["oily"] = food.oily
            result[menu["dateTime"]].append(eat_food)

    return result

def getUserPrefer(menus):
    prefer_user = {"spicy":0, "meat":0, "vegetable":0, "seafood":0, "oily":0}
    cnt = 0

    for menu in menus:
        size = len(menus[menu]) 
        # 각 날짜에 들어있는 메뉴의 가지 수 = size
        while size > 0:
            # 총 메뉴의 수 cnt (나중에 평균치 계산할 때)

            cnt += 1
            size -= 1
   
            # 각 메뉴마다 수치 더해주기
            prefer_user["spicy"] += menus[menu][size].get("spicy")
            prefer_user["meat"] += menus[menu][size].get("meat")
            prefer_user["vegetable"] += menus[menu][size].get("vegetable")
            prefer_user["seafood"] += menus[menu][size].get("seafood")
            prefer_user["oily"] += menus[menu][size].get("oily")

    # 평균내기
    if cnt:
        prefer_user["spicy"]/=cnt
        prefer_user["meat"]/=cnt
        prefer_user["vegetable"]/=cnt
        prefer_user["seafood"]/=cnt
        prefer_user["oily"]/=cnt
    else:
        prefer_user["spicy"] = 1
        prefer_user["meat"] = 1
        prefer_user["vegetable"] = 1
        prefer_user["seafood"] = 1
        prefer_user["oily"] = 1
    return prefer_user

def getFoodRecomm(prefer_user, prefer_string):
    foods = (Food.objects.filter(commercialFood="품목대표", meat = 0)
    | Food.objects.filter(commercialFood="품목대표", meat = 1)
    | Food.objects.filter(commercialFood="품목대표", meat = 2))
    
    # 사용자의 선호 식단 채소, 고기, 일반에 따라 가중치 ++
    prefer_weight = {"meat": 1 ,"vegetable": 1, "seafood": 1 , "spicy": 1, "oily": 1}

    if prefer_string == "채소": 
        prefer_weight["vegetable"] = 0.1
    elif prefer_string == "고기":
        prefer_weight["meat"] = 0.1

    # DB의 모든 Food에 대하여 점수 계산
    food_list = []
    for food in foods.values():
        food_dic = {}
        score = 0
        # item : meat, vegetable, seafood, spicy, oily
        for item in prefer_user:
            score += abs(prefer_user[item] - food[item]) * prefer_weight[item]
        # food_list.append((food["id"], food["foodName"], round(score,3)))
        food_dic["foodId"] = food["id"]
        food_dic["foodName"] = food["foodName"]
        food_dic["score"] = round(score, 2)

        foodrecommserializer = FoodRecommSerializer(data=food_dic)
        if foodrecommserializer.is_valid(raise_exception = True):
            food_list.append(foodrecommserializer.data)
        else:
            return Response({'error': 'FoodRecomm 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
    food_list.sort(key=lambda x: x["score"])

    return food_list

# 음식 상세 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def food_detail(request,foodId):
    print(foodId)
    food = get_object_or_404(Food, pk=foodId)
    print(food)
    serializer = FoodSerializer(food)
    # return HttpResponse("You're at the food_detail.")
    return Response(serializer.data)

# 추가메뉴조회
def sub_foods(request,foodId):
    return HttpResponse("sub food")
    
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
