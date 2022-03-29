# from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.permissions import AllowAny
from .serializers import WeekMenuSerializer

from menus.models import Menu, MenuToFood, Food
from menus.serializers import MenuSerializer, MenuToFoodSerializer
# import json
# Create your views here.

# 주차별 식단 기록 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def weekly_menus(request, username, firstDayOfWeek):
    # front에 보낼 data dictionary
    result_data = []
    # 하루하루의 data dictionary
    user_data = {}
    
    # 시작 날짜, 끝날 날짜 지정
    firstDayOfWeek = str(firstDayOfWeek)
    y=firstDayOfWeek[:4]
    m=firstDayOfWeek[4:6]
    d=firstDayOfWeek[6:8]

    week_start = datetime(int(y),int(m),int(d))
    week_end = datetime(int(y),int(m),int(d)) + timedelta(days=6)
    # user의 해당 기간동안의 menu DB조회
    user=get_object_or_404(get_user_model(), username=username)
    user_menus = Menu.objects.filter(userId=user.id, dateTime__range=[week_start, week_end])
    menuserializer = MenuSerializer(user_menus, read_only=True, many=True)
    # return Response(menuserializer.data)
    
    for find_menu in menuserializer.data:
        # user_data에 DB 저장해서 만들기
        user_data["dateTime"] = find_menu["dateTime"]
        user_data["mealTime"] = find_menu["mealTime"]
        mtf = MenuToFood.objects.filter(menuId=find_menu["id"])
        mtfserializer = MenuToFoodSerializer(mtf, read_only=True, many=True)
        for mtf in mtfserializer.data:
            food = get_object_or_404(Food, id=mtf["foodId"])
            user_data["foodName"] = food.foodName
            user_data["foodCategory"] = food.foodCategory
            user_data["foodDetailCategory"] = food.foodDetailCategory
            user_data["servingSize"] = food.servingSize
            user_data["foodKcal"] = food.foodKcal
            user_data["sugar"] = food.sugar
            user_data["carbohydrate"] = food.carbohydrate
            user_data["protein"] = food.protein
            user_data["fat"] = food.fat
            user_data["cholesterol"] = food.carbohydrate
            user_data["fattyAcid"] = food.fattyAcid
            user_data["amount"] = mtf["amount"]

            weekmenuserializer = WeekMenuSerializer(data=user_data)
            if weekmenuserializer.is_valid(raise_exception=True):
                result_data.append(weekmenuserializer.data)
            else:
                return Response({'error': 'menuToFood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)

    return Response(result_data, status=status.HTTP_200_OK)
    # return Response(json.dumps(result_data), status=status.HTTP_200_OK)


# 주차별 영양소 기록 조회
def weekly_nutrients(request,userId, week):
    return HttpResponse("weekly_nutrients")


# 식단 분석 데이터 조회
def data_analysis(request, userId):
    return HttpResponse("data_analysis")

