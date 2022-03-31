from django.urls import path
from . import views


app_name = 'search'

urlpatterns = [
    # 음식 검색
    path('<keyword>/', views.search_foods),
    
    # 음식 검색 후 카테고리로 분류된 리스트
    path('<keyword>/<category>/', views.search_foods_category),

    # 카테고리 별로 분류해서 보여주기
    path('aa/list/<category>/',views.search_foods_by_category)
]