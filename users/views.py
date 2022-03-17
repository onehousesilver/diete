# from django.shortcuts import render
from django.http import HttpResponse  

# 회원 가입
def join(request):
    return HttpResponse("Hello, world. Join!")

# ID 중복체크
def check_id(request, userId):
    return HttpResponse("Hello, world. check_id!")

# 회원 정보 수정
def update_user_info(request, userId):
    return HttpResponse("Hello, world. update_user_info!")

# 로그인
def login(request):
    return HttpResponse("Hello, world. login!")