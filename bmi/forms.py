from django import forms
from django.forms import widgets
from .models import Predictions
from bmi import models


class ModelForm(forms.ModelForm):
    class Meta:
        model = Predictions
        fields = [
            "height",
            "weight",
            "sex",
        ]