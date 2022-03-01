from django.urls import path

from .views import BmiPrediction

app_name = "bmiapi"

urlpatterns = [
    # bmiapi view, after root url
    path("", BmiPrediction.as_view(), name="predict_model"),
]
