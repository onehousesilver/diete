from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import FoodSerializer
from menus.models import Food

categoryDict = { "meat" : ["육류구이", "육류국.탕", "육류볶음", "육류튀김", "육류찌개.전골", "육류전", "육류조림", "육류찜", "치킨류"]
    ,"vegetable" : ["채소류구이", "채소류국.탕", "김치", "나물.숙채류", "나물.채소류무침", "채소류볶음", "채소류전", "채소류조림", "채소류찌개.전골", "채소류튀김", "샐러드", "채소류찜"]
    ,"fish" : ["어패류구이", "어패류국.탕", "회류", "어패류찜", "어패류무침", "어패류볶음", "어패류전", "어패류조림", "어패류찌개.전골", "어패류튀김"]
    ,"drink" : ["커피류","차류","과일.채소음료류","탄산음료류","스무디류","우유.유제품류","주류","기타 음료류"]
    ,"bread" : ["떡류","곡류 및 서류","중식면류","라면류","국수류","스파게티류","김밥(초밥)류","덮밥류","비빔밥류","볶음밥류","쌀밥.잡곡밥류","앙금빵류","크림빵류","피자류","샌드위치류","도넛류","케이크류","페이스트리류","죽류","리조또.그라탕류","떡볶이류","식빵류","버거류","만두류","기타 밥류","기타 빵류","기타 면류"]
    ,"snack" : ["한과류","아이스크림류","빙수류","기타 과자류","쿠키.비스킷류","초콜릿류","스낵류"]
    ,"etc" : ["기타 국류","기타 볶음류","기타","기타 생채.무침류","장아찌.절임류","적류","부침류","포류","기타 튀김류","스프류","냉국류","기타 전.적","젓갈류","기타 조림류","기타 찜류","기타 구이류","탕류"]
    }


# 카테고리만 왔을 경우
@api_view(['GET'])
@permission_classes([AllowAny])
def search_category(request, category):
    answer =[]
    if category == "":
        return Response({f'카테고리가 없습니다.'},status=status.HTTP_204_NO_CONTENT)
    elif category == "all":
        food = Food.objects.all()
        serializer = FoodSerializer(food, read_only=True, many=True)
        answer += serializer.data
        return Response(answer, status=status.HTTP_200_OK)
    else:
        for fc in categoryDict[category]:
            food = Food.objects.filter(foodDetailCategory=fc)
            serializer = FoodSerializer(food, read_only=True, many=True)
            answer += serializer.data
        return Response(answer, status=status.HTTP_200_OK)

# 카테고리와 키워드가 왔을 경우
@api_view(['GET'])
@permission_classes([AllowAny])
def search_foods_category(request, category, keyword):
    # 프론트에서 고기 누름 -> category = "meat"
    answer =[]
    if category == "":
        return Response({f'카테고리가 없습니다.'},status=status.HTTP_204_NO_CONTENT)
    elif category == "all":
        food = Food.objects.filter(foodName__icontains=keyword)
        serializer = FoodSerializer(food, read_only=True, many=True)
        answer += serializer.data
        return Response(answer, status=status.HTTP_200_OK)
    else:
        for fc in categoryDict[category]:
            food = Food.objects.filter(foodDetailCategory=fc).filter(foodName__icontains=keyword)
            serializer = FoodSerializer(food, read_only=True, many=True)
            answer += serializer.data
        return Response(answer, status=status.HTTP_200_OK)