# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# 주차별 식단 기록 조회
def weekly_menus(request, userId, week):
    return HttpResponse("weekly_menus")
# 주차별 영양소 기록 조회
def weekly_nutrients(request,userId, week):
    return HttpResponse("weekly_nutrients")
# 식단 분석 데이터 조회
def data_analysis(request, userId):
    return HttpResponse("data_analysis")

