from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='review-list'),
    path('foods/<int:pk>', views.FoodsDetailView.as_view(), name='review-detail'),
]
