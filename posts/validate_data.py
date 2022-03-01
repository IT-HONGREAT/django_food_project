from .models import Post

posts = Post.objects.all()


def validate_post():

    for post in posts:
        if "&" in post.content:
            print(f"{post.id}번글에 & 가 있습니다.")

            post.content = post.content.replace("&", "")

            post.save()
        if post.created_date > post.modified_date:

            print(f"{post.id}번글(제목:{post.title})의 생성일이 수정일보다 큽니다.")
            post.save()
