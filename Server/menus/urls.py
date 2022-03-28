from django.urls import path
from . import views


app_name = 'menus'

urlpatterns = [
    # 음식추천
    path('recommendation/<int:userId>/<int:pageNo>/',views.recommend_foods),
    
    # 음식상세조회
    path('<int:menuId>/', views.food_detail),

    # 추가메뉴조회
    path('submenu/<int:menuId>/', views.sub_foods),

    # 장바구니최종 결정
    path('basket/', views.decision_basket),
]