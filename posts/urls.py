from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post-list'),
    path('posts/<int:post_id>', views.post_detail, name='post-detail'),
    path('posts/create', views.post_create, name='post-create'),
    path('posts/<int:post_id>/edit', views.post_update, name='post-update'),
    path('posts/<int:post_id>/delete', views.post_delete, name='post-delete'),
]
