from django.contrib import admin
from django.urls import path
from . import views

app_name = 'bmi'

urlpatterns = [

    # bmiapp url
    path('predict/', views.predict_model, name='predict_model'),
    
]
