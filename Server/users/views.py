# from django.shortcuts import render
from django.http import HttpResponse  
from django.http.response import JsonResponse
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import  status
from .serializers import UserSerializer, UserProfileSerializer
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

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
def check_id(response, username):
    User = get_user_model()
    data = {'isUnique': not User.objects.filter(username=username).exists()}
    return JsonResponse(data)

# 회원 정보 수정
@api_view(['PUT'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def update_user_info(request):
    
    User = get_user_model()

    # if request.user.username != request.data.get('username') and User.objects.filter(username=request.data.get('username')).exists():
    #         return Response({'error': '일치하는 닉네임이 존재합니다.'}, status=status.HTTP_400_BAD_REQUEST)
    serializer = UserProfileSerializer(request.user, data=request.data)

    if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)