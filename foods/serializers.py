from rest_framework import serializers

from foods.models import Review

print('test',Review.objects.all())

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'title',
            'name',
            'content'
        )

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'