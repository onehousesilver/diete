from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

# AbstractUser에 기본적으로 id와 password가 있음
class User(AbstractUser):
    
    # id(PK, index), username(로그인 id), pw(로그인 pw)
    # 사용자의 실명
    name = models.CharField(max_length=10)
    # 사용자 생년월일
    birthDate = models.DateField(default=datetime.date.today)
    # 사용자의 키  0.0cm ~ 999.9cm // max_digits=숫자 전체 자리수, decimal_places=소수점 자리수
    height = models.DecimalField(max_digits=4, decimal_places=1, default=160)
    # 사용자의 몸무게 0.0kg ~ 999.9kg
    weight = models.DecimalField(max_digits=4, decimal_places=1, default=50)
    # 사용자의 활동량 적음,보통,많음 
    activity = models.CharField(default="보통", max_length=10)
    # 사용자의 성별 0 : 남자, 1 : 여자
    gender = models.IntegerField(default=1)
    # 사용자의 선호 식단 채소, 고기, 일반
    preference = models.CharField(default="일반", max_length=10)
    # 사용자의 권장 칼로리
    kcal = models.IntegerField(default=1500)

    # USERNAME_FIELD = 'userId'

    
    # Menu테이블과 1:n으로 연결 필요

# userName이 AbstractUser에 기본 제공되어 duplicate column name: userName Error 발생!
# createsuperuser 생성 시 default 값이 없으면 migrate가 잘 되어도 data가 들어가지 않는 이슈 발생.