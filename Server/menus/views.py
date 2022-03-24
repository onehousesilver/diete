from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import get_object_or_404
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
    
# 장바구니 최종 결정 + 식단수정
@api_view(['POST', 'PUT'])
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
        
    elif request.method == 'PUT':
        pass