from django import forms
from django.forms import widgets
from .models import Review, User
from foods import models


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
        ]
        widgets = {
            "intro": forms.Textarea,
        }
