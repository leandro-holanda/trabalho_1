from rest_framework import generics
from rest_framework.permissions import IsAdminUser
from .serializers import ActorModelSerializer
from .models import Actor


class ActorCreateListView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
    permission_classes = [IsAdminUser,]


class ActorRetrieveUpdateDestroyView(generics.ListCreateAPIView):
    queryset = Actor.objects.all()
    serializer_class = ActorModelSerializer
    permission_classes = [IsAdminUser,]