from rest_framework import serializers
from .models import Movie
from genres.models import Genre
from actors.models import Actor


class MovieModelSerializer(serializers.ModelSerializer):
    genre = serializers.SerializerMethodField()
    actors = serializers.SerializerMethodField()
    genre_ids = serializers.PrimaryKeyRelatedField(
        queryset=Genre.objects.all(), many=True, write_only=True
    )
    actor_ids = serializers.PrimaryKeyRelatedField(
        queryset=Actor.objects.all(), many=True, write_only=True
    )
    
    class Meta:
        model = Movie
        fields = '__all__'

    def get_actors(self, obj):
        return [actor.name for actor in obj.actors.all()]
    
    def get_genre(self, obj):
        return [genre.name for genre in obj.genre.all()]

    def update(self, instance, validated_data):
        genre_ids = validated_data.pop('genre_ids', None)
        actor_ids = validated_data.pop('actor_ids', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        if genre_ids is not None:
            instance.genre.set(genre_ids)
        if actor_ids is not None:
            instance.actors.set(actor_ids)

        return instance