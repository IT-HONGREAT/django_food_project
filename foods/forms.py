from django import forms
from .models import Review, User


class Signupform(forms.ModelForm):
    class Meta:
        model = User
        fields = ["nickname"]

    def signup(self, request, user):

        user.nickname = self.cleaned_data["nickname"]
        user.save()


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
