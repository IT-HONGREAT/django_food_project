from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    # path('menu/<int:pk>/', views.food_detail),
    path('foods/<int:pk>', views.FoodsDetailView.as_view(), name='review-detail'),
]
