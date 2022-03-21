from django.http import HttpResponse

# Create your views here.
# 음식 검색
def search_foods(request, keyword):
    return HttpResponse("search_foods")

# 음식 검색 후 카테고리로 분류된 리스트
def search_foods_category(request, keyword, category):
    return HttpResponse("search_foods_category")
