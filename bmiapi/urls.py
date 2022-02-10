from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BmiPrediction

app_name = 'bmi'

urlpatterns = [

    # ml 관련 urls
    path('predict/', BmiPrediction.as_view(), name='predict_model'),
    
]

