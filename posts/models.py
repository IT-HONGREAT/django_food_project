from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.fields.files import ImageField
from .validators import validate_numbers
# Create your models here.


# 단기적인 구상(수정_필요) : 음식이름, 음식 이미지, 음식에 대한 나의 의견?/기분?, 평점, 작성일(먹은 날짜가 아닐 수도 있음..), 수정일,

class Post(models.Model):

    title = models.CharField(max_length=100)
    food_img = models.ImageField(upload_to='food_img/')
    created_date = models.DateTimeField(auto_now_add=True)
    feeling = models.CharField(max_length=80, default='')
    score = models.IntegerField(default=0)
    content = models.TextField(
        validators=[MinLengthValidator(3, '음식의 설명이나 기분을 3글자 이상 적어주세요!'),
                    validate_numbers])

    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
