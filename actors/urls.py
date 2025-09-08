from django.urls import path
from .views import ActorCreateListView, ActorRetrieveUpdateDestroyView


urlpatterns = [
    path('actors/', ActorCreateListView.as_view(), name='actor_create_list'),
    path('actors/<int:pk>/', ActorRetrieveUpdateDestroyView.as_view(), name='actor_update_delete'),
]