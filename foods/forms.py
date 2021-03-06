from django import forms

from .models import Review, User, Comment


# class Signupform(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ["nickname"]

#     def signup(self, request, user):

#         user.nickname = self.cleaned_data["nickname"]
#         user.save()


class Reviewform(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            "title",
            "name",
            "place_link",
            "rating",
            "image_1",
            "image_2",
            "image_3",
            "content",
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            "nickname",
            "profile_img",
            "intro",
            "height",
            "weight",
            "sex",
        ]
        widgets = {
            "intro": forms.Textarea,
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment"]

    def __init__(self, *args, **kwargs):

        self.request = kwargs.pop("request", None)
        super(CommentForm, self).__init__(*args, **kwargs)
