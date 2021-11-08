from django.shortcuts import render
from .models import Post
# Create your views here.

def post_list(request):

    posts = Post.objects.all()
    context  = {"posts" : posts}

    return render(request, 'posts/post_list.html', context)


def post_detail(request,pk):

    context = dict()
    post = Post.objects.get(id=pk)
    context  = {"post" : post}
    return render(request, 'posts/post_detail.html', context)