from django.conf.urls import url
from django.db.models.base import Model
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView
from django.urls import reverse
from posts.forms import PostForm
from .models import Post
# Create your views here.


class PostListView(ListView):

    model = Post
    template_name = 'posts/post_list.html'
    context_object_name = 'posts'
    ordering = ['-created_date']
    paginate_by = 6
    page_kwarg = 'page'


class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/post_detail.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'


# def post_create(request):
#     # request를 통해서 들어온 것을 post인지 구분하게 해야함
#     if request.method == 'POST':

#         post_form = PostForm(request.POST, request.FILES)
#         if post_form.is_valid():  # 유효성검증을 해주는 조건문
#             new_post = post_form.save()
#             return redirect('post-detail', post_id=new_post.id)

#     # get방식 일 때, 폼을 돌려주는 원래 페이지로 줌
#     else:
#         post_form = PostForm()
#     return render(request, 'posts/post_form.html', {'form': post_form})


# class PostCreateView(CreateView):
#     model = Post
#     form_class = PostForm
#     template_name = 'posts/post_form.html'


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})


# def post_update(request, post_id):

#     post = get_object_or_404(Post, id=post_id)

#     if request.method == 'POST':
#         post_form = PostForm(request.POST, instance=post)
#         if post_form.is_valid():
#             post_form.save()
#             return redirect('post-detail', post_id=post.id)

#     else:
#         post_form = PostForm(instance=post)

#     post_form = PostForm(instance=post)
#     return render(request, 'posts/post_form.html', {'form': post_form})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'
    pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})


def post_delete(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'posts/post_delete_confirm.html', {'post': post})


def index(request):
    return redirect('post-list')
