from django.conf.urls import url
from django.db.models.base import Model
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView, RedirectView
from django.urls import reverse
from posts.forms import PostForm
from .models import Post
# Create your views here.


# def index(request):
#     return redirect('post-list')
class IndexRedirectView(RedirectView):

    pattern_name = 'post-list'


class PostListView(ListView):

    model = Post
    ordering = ['-created_date']
    paginate_by = 6


class PostDetailView(DetailView):
    model = Post
    # template_name = 'posts/post_detail.html'  # 모델명_각뷰이름.html이 기본값, 자동 적용
    # pk_url_kwarg = 'post_id'         # url 에서 pk가 기본 값이기 때문에 변경해주면 삭제해도됨
    # context_object_name = 'post'   # 제너릭의 기본 값 모델을 소문자로 쓰면됨


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    # template_name = 'posts/post_form.html'
    # pk_url_kwarg = 'post_id'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'pk': self.object.id})


class PostDeleteView(DeleteView):

    model = Post
    # template_name = 'posts/post_delete_confirm.html'
    # pk_url_kwarg = 'post_id'
    # context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')
