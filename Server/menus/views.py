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
        menudata = {
            "userId" : user.id,
            "date" : datetime.now().date(),
            "mealTime" : request.data["mealTime"]
        }
        menuserializer = MenuSerializer(data=menudata)
        if menuserializer.is_valid():
            menuserializer.save()
            # menu에서 저장될 때 생성된 id 저장 (MenuToFood를 위해서)
            menuTempId = menuserializer.data["id"]

        menus_amount = serializers.ListField(request.data["menus"])
        print(menus_amount)
        # for menu in menus_amount:
        #     mtfdata = {
        #         "foodId" : menu[0],
        #         "menuId" : menuTempId,
        #         "amount" : menu[1],
        #     }
        #     mtfserializer = MenuToFoodSerializer(data=mtfdata)
        #     if mtfserializer.is_valid():
        #         mtfserializer.save()
        return Response(menuserializer.data)
        # return Response({menuserializer.data, mtfserializer.data}, many=True)

