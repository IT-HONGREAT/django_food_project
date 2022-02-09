from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bmi'

urlpatterns = [

    # ml 관련 urls
    path('bmi/predict', views.predict_model, name='predict_model'),
    
]
