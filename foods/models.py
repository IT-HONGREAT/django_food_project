from django.contrib.auth.models import AbstractUser
from django.db import models

from .validators import validate_no_special_characters, validate_no_place_link


class User(AbstractUser):
    nickname = models.CharField(
        max_length=20,
        unique=True,
        null=True,
        error_messages={"unique": "이미 사용중인 닉네임입니다"},
        validators=[validate_no_special_characters],
    )
    gender_choice = [
        ("0", "여"),  # 여자
        ("1", "남"),  # 남자
    ]

    profile_img = models.ImageField(default="default_profile_img", upload_to="profile_img")

    intro = models.CharField(max_length=60, blank=True)
    sex = models.CharField(max_length=2, choices=gender_choice)
    height = models.IntegerField(default=1)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return self.email


class Review(models.Model):
    title = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    place_link = models.URLField(validators=[validate_no_place_link])  # 네이버, 카카오 링크 연결

    rating_choice = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    rating = models.IntegerField(choices=rating_choice)

    image_1 = models.ImageField(upload_to="food_img/")
    image_2 = models.ImageField(upload_to="food_img/", blank=True)
    image_3 = models.ImageField(upload_to="food_img/", blank=True)
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    post = models.ForeignKey(Review, on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment
