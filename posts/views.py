from django.conf.urls import url
from django.db.models.base import Model
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
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


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})


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


class PostDeleteView(DeleteView):

    model = Post
    template_name = 'posts/post_delete_confirm.html'
    pk_url_kwarg = 'post_id'
    context_object_name = 'post'

    def get_success_url(self):
        return reverse('post-list')


def index(request):
    return redirect('post-list')
