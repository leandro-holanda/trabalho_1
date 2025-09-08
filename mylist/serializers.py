from rest_framework import serializers
from .models import MyList


class MyListModelSerializer(serializers.ModelSerializer):
    movie = serializers.SerializerMethodField()

    class Meta:
        model = MyList
        fields = ('movie',)

    def get_movie(self, obj):
        return obj.movie.title