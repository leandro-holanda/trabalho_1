from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import MyList
from .serializers import MyListModelSerializer
from movies.models import Movie
from rest_framework.exceptions import ValidationError


class MyListCreateListView(generics.ListCreateAPIView):
    serializer_class = MyListModelSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return MyList.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        movie_input = self.request.data.get('movie')

        if not movie_input:
            raise ValidationError({"movie": "Você precisa informar o filme (nome ou ID)."})
        
        try:
            movie = Movie.objects.get(id=int(movie_input))
        except (ValueError, Movie.DoesNotExist):
           
            try:
                movie = Movie.objects.get(title__iexact=movie_input)
            except Movie.DoesNotExist:
                raise ValidationError({"movie": f"Filme '{movie_input}' não encontrado."})

        serializer.save(user=self.request.user, movie=movie)


class MyListRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MyListModelSerializer
    permission_classes = [IsAuthenticated,]

    def get_queryset(self):
        return MyList.objects.filter(user=self.request.user)