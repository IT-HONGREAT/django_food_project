from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BmiPrediction

app_name = 'bmi'

urlpatterns = [

    # bmiapi view, after root url
    path('predict/', BmiPrediction.as_view(), name='predict_model'),
    
]

