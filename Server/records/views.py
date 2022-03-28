# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

from rest_framework.response import Response

from menus.models import Menu, MenuToFood, Food
# Create your views here.

# 주차별 식단 기록 조회
def weekly_menus(request, username, week):
    # 사용자 모델 가져오기
    # 필요없을지도?
    # user = get_object_or_404(get_user_model(), username=request.user.username)
    # 사용자 id와 일치하는 
    menu = get_list_or_404(Menu, username = request.user.username)

    return Response(menu)


# 주차별 영양소 기록 조회
def weekly_nutrients(request,userId, week):
    return HttpResponse("weekly_nutrients")


# 식단 분석 데이터 조회
def data_analysis(request, userId):
    return HttpResponse("data_analysis")

