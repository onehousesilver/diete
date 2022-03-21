# from django.shortcuts import render
from django.http import HttpResponse  
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import  status
from .serializers import UserSerializer

# 회원 가입
@api_view(['POST'])
@permission_classes([AllowAny])
def join(request):
    password = request.data.get('password')
    # password_confirmation = request.data.get('passwordConfirmation')
    
    # if password != password_confirmation:
    #     return Response({'error' :'비밀번호가 일치하지 않습니다.'}, status = status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# ID 중복체크
@api_view(['GET'])
@permission_classes([AllowAny])
def check_id(response, userId):
    User = get_user_model()
    data = {'isUnique': not User.objects.filter(userId=userId).exists()}
    return JsonResponse(data)

# 회원 정보 수정
def update_user_info(request, userId):
    print(userId)
    return HttpResponse("Hello, world. update_user_info!")

# 로그인
# def login(request):
#     return HttpResponse("Hello, world. login!")