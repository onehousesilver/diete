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
    serializer = UserSerializer(data=request.data)
    
    if serializer.is_valid(raise_exception=True):
    # 키 몸무게 성별을 고려한 kcal 계산
        H = int(request.data.get('height'))
        W = int(request.data.get('weight'))
        a = int(request.data.get('activity'))
        g = int(request.data.get('gender'))
        # 활동량이 적을 경우(ACTIVITY = 0)
        if a == 0:
            # 남자인 경우(GENDER = 0)
            if g == 0:
                avgKg = (H/100)**2 * 22
                kcal = avgKg * 27
                print(avgKg)
                print(kcal)

            # 여자인 경우(GENDER = 1)    
            elif g == 1:
                avgKg = (H/100)**2 * 21
                kcal = avgKg * 27
               
        # 활동량이 보통일 경우(ACTIVITY = 0)        
        elif a == 1:
            if g == 0:
                avgKg = (H/100)**2 * 22
                kcal = avgKg * 33
            elif g == 1:
                avgKg = (H/100)**2 * 21
                kcal = avgKg * 33

        # 활동량이 많을 경우(ACTIVITY = 2)
        elif a == 2:
            if g == 0:
                avgKg = (H/100)**2 * 22
                kcal = avgKg * 38
            elif g == 1:
                avgKg = (H/100)**2 * 21
                kcal = avgKg * 38
        
        user = serializer.save()
        user.set_password(password)
        user.kcal = kcal
        user.save()
    # 선호 식단을 골랐을 떄 들어가는 식단
        return Response(serializer.data, status=status.HTTP_201_CREATED)



# ID 중복체크
@api_view(['GET'])
@permission_classes([AllowAny])
def check_id(response, userId):
    User = get_user_model()
    data = {'isUnique': not User.objects.filter(userId=userId).exists()}
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