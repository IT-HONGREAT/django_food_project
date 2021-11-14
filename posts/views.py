from posts.forms import PostForm
from django.shortcuts import redirect, render
from .models import Post
# Create your views here.


def post_list(request):

    posts = Post.objects.all()
    context = {"posts": posts}

    return render(request, 'posts/post_list.html', context)


def post_detail(request, post_id):

    context = dict()
    post = Post.objects.get(id=post_id)
    context = {"post": post}
    return render(request, 'posts/post_detail.html', context)


def post_create(request):
    # request를 통해서 들어온 것을 post인지 구분하게 해야함
    if request.method == 'POST':
        # title = request.POST['title'],
        # content = request.POST['content'],
        # new_post = Post(
        #     title=title,
        #     content=content,
        # )
        # new_post.save()
        post_form = PostForm(request)
        new_post = post_form.save()
        return redirect('post-detail', post_id=new_post.id)

    # get방식 일 때, 폼을 돌려주는 원래 페이지로 줌
    else:
        post_form = PostForm
        return render(request, 'posts/post_form.html', {'form': post_form})
