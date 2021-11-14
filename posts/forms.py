from django import forms
from django.forms.widgets import Textarea
from .models import Post


# class PostForm(forms.Form):
#     title = forms.CharField(max_length=50, label='제목')
#     content = forms.CharField(label='내용', widget=forms.Textarea)
#     feeling = forms.CharField(max_length=80, label='식후 상태')
#     score = forms.IntegerField(label='음식 점수')
#     dt_created = forms.DateField(label='날짜')

class PostForm(forms.ModelForm):  # 장고제공_모델폼으로 수정( 위의 기존 틀과 상이)

    class Meta:
        model = Post
        fields = ['title', 'food_img', 'feeling',
                  'score', 'content']  # 선택 출력 (date는 안불러와짐)
        # fields = '__all__'  # 전체 출력
