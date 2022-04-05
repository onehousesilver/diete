# from django.shortcuts import render
from datetime import datetime, timedelta
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,  permission_classes
from rest_framework.permissions import AllowAny
from menus.models import Menu, MenuToFood, Food
from menus.serializers import MenuSerializer, MenuToFoodSerializer

from datetime import date
# import json
# Create your views here.

# 주차별 식단 기록 조회
@api_view(['GET'])
@permission_classes([AllowAny])
def weekly_menus(request, username, firstDayOfWeek):
    # front에 보낼 data dictionary
    result_data = []
    # 하루하루의 data dictionary
    response_data = []
    
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
        print(find_menu)
        user_data = {}
        user_data["dateTime"] = find_menu["dateTime"]
        user_data["mealTime"] = find_menu["mealTime"]
        mtf = MenuToFood.objects.filter(menuId=find_menu["id"])
        mtfserializer = MenuToFoodSerializer(mtf, read_only=True, many=True)
        user_data["menus"] = []
        for mtf in mtfserializer.data:
            food_data = {}
            food = get_object_or_404(Food, id=mtf["foodId"])
            food_data["foodName"] = food.foodName
            food_data["foodCategory"] = food.foodCategory
            food_data["foodDetailCategory"] = food.foodDetailCategory
            food_data["servingSize"] = food.servingSize
            food_data["foodKcal"] = food.foodKcal
            food_data["sugar"] = food.sugar
            food_data["carbohydrate"] = food.carbohydrate
            food_data["protein"] = food.protein
            food_data["fat"] = food.fat
            food_data["cholesterol"] = food.carbohydrate
            food_data["fattyAcid"] = food.fattyAcid
            food_data["amount"] = mtf["amount"]

            user_data["menus"].append(food_data)
        result_data.append(user_data)
        response_data.append(result_data)
        # if weekmenuserializer.is_valid(raise_exception=True):
        # else:
            # return Response({'error': 'menuToFood 테이블 삽입 에러'}, status=status.HTTP_400_BAD_REQUEST)
    

    return Response(result_data, status=status.HTTP_200_OK)
    # return Response(json.dumps(result_data), status=status.HTTP_200_OK)
    
# 주차별 영양소 기록 조회
def weekly_nutrients(request,userId, week):
    return HttpResponse("weekly_nutrients")


# 식단 분석 데이터 조회
def data_analysis(request, userId):
    return HttpResponse("data_analysis")


# 식단 분석 - 일별 총 칼로리
@api_view(['GET'])
@permission_classes([AllowAny])
def oneday_kcal(request, username):
    # 유저 검색
    user=get_object_or_404(get_user_model(), username=username)
    # 유저가 입력한 menu 검색
    user_oneday = Menu.objects.filter(userId=user.id)

    # day_id_dict = {"2000-01-01" : [menuId1, menuId2], ...}
    day_id_dict = {}
    for user_menu in user_oneday:
        # dummydata 제외
        if user_menu.dateTime == date(2000,1,1):
            pass
        else:
            if user_menu.dateTime in day_id_dict:
                day_id_dict[user_menu.dateTime].append(user_menu.id)
            else:
                day_id_dict[user_menu.dateTime] = [user_menu.id]
    # print(day_id_dict)

    # 반환값 : daily_kcal = [ {"dateTime": "2000-01-01", "kcal": 5340 }, {}]
    daily_kcal = []
    for key in day_id_dict.keys():
        total_kcal = total_sugar = total_carbo = total_protein = 0
        total_fat = total_cholesterol = total_fatty = 0

        for menuId in day_id_dict[key]:
            mtfs = MenuToFood.objects.filter(menuId =menuId)
            for mtf in mtfs:
                total_kcal += mtf.foodId.foodKcal * mtf.amount
                total_sugar += mtf.foodId.sugar * mtf.amount
                total_carbo += mtf.foodId.carbohydrate * mtf.amount
                total_protein += mtf.foodId.protein * mtf.amount
                total_fat += mtf.foodId.fat * mtf.amount
                total_cholesterol += mtf.foodId.cholesterol * mtf.amount
                total_fatty += mtf.foodId.fattyAcid * mtf.amount

        # print(total_kcal)
        daily_kcal.append({"dateTime": key, "total_kcal": total_kcal, "total_sugar" : total_sugar, "total_carbo" : total_carbo, 
        "total_protein" : total_protein, "total_fat": total_fat, "total_cholesterol": total_cholesterol, "total_fatty": total_fatty })
    # print(daily_kcal)
    
    return JsonResponse(daily_kcal, safe=False)