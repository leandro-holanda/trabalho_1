from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Movie
from .serializers import MovieModelSerializer


class MovieCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    permission_classes = [IsAdminUser,]


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    permission_classes = [IsAuthenticated,]


class MovieRetrieveUpdateDestroytView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    permission_classes = [IsAdminUser,]