from django.urls import path
from . import views


app_name = 'records'

urlpatterns = [
    # 주차별 식단 기록 조회
    path('menu/<username>/<int:firstDayOfWeek>/', views.weekly_menus),
    # 끼니별 영양소 기록 조회 - 주간
    path('nutrients/<username>/<int:firstDayOfWeek>/', views.weekly_nutrients),
    # 식단 분석 - 일별 총 칼로리
    path('<username>/', views.data_analysis),
    # 식단 분석 데이터 조회
    path('<username>/<int:firstDayOfWeek>/', views.average_nutrients),
]