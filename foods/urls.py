from django.contrib import admin
from django.urls import path, include
from . import views
from foods.views import FoodListAPIView, DetailUpdateView

urlpatterns = [

    # review 관련 urls
    path('', views.IndexView.as_view(), name='review-list'),
    path('foods/<int:pk>', views.ReviewDetailView.as_view(), name='review-detail'),
    path('foods/create', views.ReviewCreateView.as_view(), name='review-create'),
    path('foods/<int:pk>/edit',
         views.ReviewUpdateView.as_view(), name='review-update'),
    path('foods/<int:pk>/delete',
         views.ReviewDeleteView.as_view(), name='review-delete'),

    # profile 관련 urls
    path('users/<int:pk>',
         views.ProfileView.as_view(), name='profile'),
    path('users/<int:pk>/reviews/',
         views.UserReviewListView.as_view(), name='user-review-list'),
    path("set-profile/", views.ProfileSetView.as_view(), name="profile-set"),
     path("edit-profile/", views.ProfileUpdateView.as_view(), name="profile-update"),

     #rest_framework
     path('foods/apiview', FoodListAPIView.as_view()),
     path('foods/apiview/<int:pk>', DetailUpdateView.as_view()),
]