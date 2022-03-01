from django import forms

from .models import Predictions


class ModelForm(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = [
            "height",
            "weight",
            "sex",
        ]
