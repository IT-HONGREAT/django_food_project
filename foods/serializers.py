from rest_framework import serializers

from foods.models import Review, User

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

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'