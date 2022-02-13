from rest_framework import serializers
from .models import Predictions

class PredictionsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Predictions
        fields = [
            "height",
            "weight",
            "sex",
        ]
        