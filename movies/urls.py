from django.urls import path
from .views import MovieRetrieveUpdateDestroyView, MovieListView, MovieCreateView


urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroyView.as_view(), name='movie_update_delete'),
]