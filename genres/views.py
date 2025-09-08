from rest_framework import generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .serializers import GenreModelSerializer
from .models import Genre


class GenreListView(generics.ListAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    permission_classes = [IsAuthenticated, ]


class GenreCreateView(generics.CreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    permission_classes = [IsAdminUser,]


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreModelSerializer
    
    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
