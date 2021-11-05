from django.db import models

# Create your models here.


# 단기적인 구상(수정_필요) : 음식이름, 음식 이미지, 음식에 대한 나의 의견?/기분?, 평점, 작성일(먹은 날짜가 아닐 수도 있음..), 수정일, 

class Post(models.Model):


    title = models.CharField(max_length=100)  
    food_img = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
        
    content = models.TextField()
        
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title