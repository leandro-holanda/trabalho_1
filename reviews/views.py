from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Review
from .serializers import ReviewModelSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
    permission_classes = [IsAuthenticated,]


class ReviewRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer
    permission_classes = [IsAuthenticated,]