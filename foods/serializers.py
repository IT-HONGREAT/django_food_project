from rest_framework import serializers

from foods.models import Review, User

print('test',Review.objects.all())

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        # fields = "__all__"
        fields = (
            'title',
            'name',
            'place_link',
            'image_1',
            'image_2',
            'image_3',
            'content',
        )

class ReviewDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'