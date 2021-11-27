from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.fields.files import ImageField
from .validators import validate_numbers
# Create your models here.


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
