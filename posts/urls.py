from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('posts/', views.PostListView.as_view(), name='post-list'),
    path('posts/<int:post_id>', views.PostDetailView.as_view(), name='post-detail'),
    path('posts/create', views.PostCreateView.as_view(), name='post-create'),
    path('posts/<int:post_id>/edit',
         views.PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:post_id>/delete',
         views.PostDeleteView.as_view(), name='post-delete'),
]
