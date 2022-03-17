from django.http import HttpResponse

# 음식 추천
def recommend_foods(request,userId,pageNo):
    return HttpResponse("recom food")

# 음식 상세 조회
def food_detail(request,menuId):
    return HttpResponse("Hello, world. You're at the food_detail.")

# 추가메뉴조회
def sub_foods(request,menuId):
    return HttpResponse("sub food")
    
# 장바구니 최종 결정
def decision_basket(request):
    return HttpResponse("basket")