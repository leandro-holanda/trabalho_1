from django.urls import path
from .views import GenreCreateListView, GenreRetrieveUpdateDestroyView


urlpatterns = [
    path('genres/', GenreCreateListView.as_view(), name='genres_create_list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genres_update_delete'),
]