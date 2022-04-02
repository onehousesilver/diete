from django.urls import path
from . import views


app_name = 'records'

urlpatterns = [
    # 주차별 식단 기록 조회
    path('menu/<username>/<int:firstDayOfWeek>/', views.weekly_menus),
    # 주차별 영양소 기록 조회
    path('nutrients/<int:userId>/<int:week>/', views.weekly_nutrients),
    # 식단 분석 데이터 조회
    path('<int:userId>/', views.data_analysis),
    # 식단 분석 - 일별 총 칼로리
    path('<username>/', views.oneday_kcal),
]