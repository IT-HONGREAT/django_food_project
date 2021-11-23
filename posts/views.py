from django.conf.urls import url
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator
from django.views.generic import CreateView
from django.urls import reverse
from posts.forms import PostForm
from .models import Post
# Create your views here.


def post_list(request):

    posts = Post.objects.all()
    paginator = Paginator(posts, 6)
    curr_page_number = request.GET.get('page')
    if curr_page_number is None:
        curr_page_number = 1
    page = paginator.page(curr_page_number)  # 페이지 번호에 해당하는 페이지를 가져옴
    return render(request, 'posts/post_list.html', {'page': page})


def post_detail(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'posts/post_form.html'

    def get_success_url(self):
        return reverse('post-detail', kwargs={'post_id': self.object.id})


def post_update(request, post_id):

    post = get_object_or_404(Post, id=post_id)

    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post=detail', post_id=post.id)

    else:
        post_form = PostForm(instance=post)

    post_form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': post_form})


def post_delete(request, post_id):

    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post-list')
    else:
        return render(request, 'posts/post_delete_confirm.html', {'post': post})


def index(request):
    return redirect('post-list')
