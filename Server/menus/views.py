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
from .serializers import FoodSerializer, MenuSerializer, MenuToFoodSerializer

from datetime import datetime
# 음식 추천
def recommend_foods(request,userId,pageNo):
    return HttpResponse("recom food")

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
def getUserPrefer(request):
    prefer_user = {"spicy":0, "meat":0, "vegetable":0, "seafood":0, "oily":0}
    cnt = 0

    for menu in menus:
        print(cnt)
        size = len(menus[menu]) 
        # 각 날짜에 들어있는 메뉴의 가지 수 = size
        while size > 0:
            # 총 메뉴의 수 cnt (나중에 평균치 계산할 때)
            cnt += 1
            size -= 1
 
            print("ㅡㅡㅡㅡㅡstartㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
            print(menus[menu][size].get("foodName"))
            print(menus[menu][size].get("spicy"))
            print(menus[menu][size].get("meat"))
            print(menus[menu][size].get("vegetable"))
            print(menus[menu][size].get("seafood"))
            print(menus[menu][size].get("oily"))
            
            # 각 메뉴마다 수치 더해주기
            prefer_user["spicy"] += menus[menu][size].get("spicy")
            prefer_user["meat"] += menus[menu][size].get("meat")
            prefer_user["vegetable"] += menus[menu][size].get("vegetable")
            prefer_user["seafood"] += menus[menu][size].get("seafood")
            prefer_user["oily"] += menus[menu][size].get("oily")
            print("ㅡㅡㅡㅡㅡendㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ")
    # 평균내기
    prefer_user["spicy"]/=cnt
    prefer_user["meat"]/=cnt
    prefer_user["vegetable"]/=cnt
    prefer_user["seafood"]/=cnt
    prefer_user["oily"]/=cnt
    print(prefer_user)
    return prefer_user
