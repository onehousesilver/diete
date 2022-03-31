from django.urls import path
from . import views


app_name = 'search'

urlpatterns = [
    # 음식 검색
    path('<category>/', views.search_category),
    path('<category>/<keyword>/', views.search_foods_category),
]