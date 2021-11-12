from django import forms
from django.forms.widgets import Textarea


class PostForm(forms.Form):
    title = forms.CharField(max_length=50, label='제목')
    content = forms.CharField(label='내용', widget=forms.Textarea)
    feeling = forms.CharField(max_length=80, label='식후 상태')
    score = forms.IntegerField(label='음식 점수')
    dt_created = forms.DateField(label='날짜')
