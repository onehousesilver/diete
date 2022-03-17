from django.urls import path
from . import views


app_name = 'users'

urlpatterns = [
    path('join/', views.join),
    path('id/<int:userId>/', views.check_id),
    path('update/<int:userId>/', views.update_user_info),
    path('login/', views.login),
    
]