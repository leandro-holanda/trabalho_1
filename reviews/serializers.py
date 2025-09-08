from rest_framework import serializers
from .models import Review


class ReviewModelSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = Review
        fields = ('id', 'movie', 'stars', 'comment', )

    def get_movie(self, obj):
        return obj.movie.title