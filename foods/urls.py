from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='review-list'),
    path('foods/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
    path('foods/create', views.ReviewCreateView.as_view(), name='review-create'),
    path('foods/<int:pk>/edit',
         views.ReviewUpdateView.as_view(), name='review-update'),
    path('foods/<int:pk>/delete',
         views.ReviewDeleteView.as_view(), name='review-delete'),
]
