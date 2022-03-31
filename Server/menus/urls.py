from django.urls import path
from . import views


app_name = 'menus'

urlpatterns = [
    # 음식추천
    path('recommendation/<username>/',views.recommend_foods),
    
    # 음식상세조회
    path('<int:foodId>/', views.food_detail),

    # 추가메뉴조회
    path('submenu/<int:menuId>/', views.sub_foods),

    # 장바구니최종 결정
    path('basket/', views.decision_basket),
    
    # 장바구니 수정
    path('basket/<int:menuId>/', views.update_basket),
]