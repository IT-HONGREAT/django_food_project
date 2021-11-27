from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    pass


class Menu(models.Model):
    name = models.CharField(max_length=50)
    calorie = models.IntegerField()
    description = models.CharField(max_length=100)
    img_path = models.CharField(max_length=255)

    def __str__(self):
        return self.name
