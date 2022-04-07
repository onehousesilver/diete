from django.db import models
import datetime

# Create your models here.
class WeekMenu(models.Model):
    # 날짜 - 사용자가 식단을 먹은 날짜
    dateTime = models.DateField(default=datetime.date.today)
    # 식사시간 - 아침, 점심, 저녁 // 0, 1, 2
    mealTime = models.IntegerField(default=0)

    # 음식 이름
    foodName= models.CharField(max_length=100)
    # 식품 대분류
    foodCategory = models.CharField(max_length=100)
    # 식품 상세분류
    foodDetailCategory = models.CharField(max_length=100)
    # 1회 제공량 - 157
    servingSize = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 열량 - 소수점 아래 8자리까지, 최대 999.~
    foodKcal = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 당류 (총당류[단위 : g]) 최대 99
    sugar = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 탄수화물
    carbohydrate = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 단백질
    protein = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 지방
    fat = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 콜레스테롤
    cholesterol = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 총 포화지방산
    fattyAcid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    # 음식 이미지
    # image = models.CharField(default=200)

    # 수량 - 해당 음식의 수량
    amount = models.IntegerField(default=1)