from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import FoodSerializer
from menus.models import Food


# Create your views here.
# 음식 검색
@api_view(['GET'])
@permission_classes([AllowAny])
def search_foods(request, keyword):
    print("search_foods start~!")
    print(keyword)
    food = Food.objects.filter(foodName__icontains=keyword)
    print(food)
    if len(food) > 0 :
        print("Hi!")
        serializer = FoodSerializer(food, read_only=True, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({f'{keyword}와(과) 일치하는 음식이 없습니다.'},status=status.HTTP_204_NO_CONTENT)

# 음식 검색 후 카테고리로 분류된 리스트
# 프론트에서 받아온 String을
@api_view(['GET'])
@permission_classes([AllowAny])
def search_foods_category(request, keyword, category):
    print("search_foods_category start~!")
    print(keyword)
    food = Food.objects.filter(foodName__icontains=keyword).filter(foodCategory=category)
    print(food)
    if len(food) > 0 :
        print("Hi!")
        serializer = FoodSerializer(food, read_only=True, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({f'{category}의 {keyword}와(과) 일치하는 음식이 없습니다.'},status=status.HTTP_204_NO_CONTENT)
