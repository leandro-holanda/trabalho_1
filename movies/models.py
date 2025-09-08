from django.db import models
from genres.models import Genre
from actors.models import Actor


class Movie(models.Model):
    title = models.CharField(max_length=250)
    genre = models.ManyToManyField(Genre)
    actors = models.ManyToManyField(Actor)
    release_date = models.DateField()
    description = models.TextField(max_length=600)

    def __str__(self):
        return self.title