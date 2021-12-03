from django.db import models
from django.contrib.auth.models import AbstractUser
from .validators import validate_no_special_characters
# Create your models here.


class User(AbstractUser):

    nickname = models.CharField(max_length=20,
                                unique=True,
                                null=True,
                                error_messages={'unique': '이미 사용중인 닉네임입니다'},
                                validators=[validate_no_special_characters],
                                )

    def __str__(self):
        return self.email

# review로 변경 전 저장


class Menu(models.Model):
    name = models.CharField(max_length=50)
    calorie = models.IntegerField()
    description = models.CharField(max_length=100)
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Review모델 싱크 완성후 Menu모델 삭제 고려


class Review(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    info_link = models.URLField()  # 네이버, 카카오 링크 연결
