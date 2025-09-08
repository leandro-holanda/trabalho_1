from django.db.models import Avg
from rest_framework import serializers
from .models import Movie
from genres.serializers import GenreModelSerializer
from actors.serializers import ActorModelSerializer


class MovieModelSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()
    
    class Meta:
        model = Movie
        fields = '__all__'

    def get_actors(self, obj):
        return [actor.name for actor in obj.actors.all()]
    
    def get_genre(self, obj):
        return [genre.name for genre in obj.genre.all()]