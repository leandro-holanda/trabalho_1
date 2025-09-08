from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import Movie
from .serializers import MovieModelSerializer


class MovieListView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    permission_classes = [IsAuthenticated, ]


class MovieCreateView(generics.CreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    permission_classes = [IsAdminUser,]


class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
