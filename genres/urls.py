from django.urls import path
from .views import GenreListView, GenreRetrieveUpdateDestroyView, GenreCreateView


urlpatterns = [
    path('genres/', GenreListView.as_view(), name='genres_create_list'),
    path('genres/create/', GenreCreateView.as_view(), name='genres_update_delete'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genres_update_delete'),
]