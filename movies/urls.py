from django.urls import path
from .views import MovieListView, MovieRetrieveUpdateDestroytView, MovieCreateView


urlpatterns = [
    path('movies/', MovieListView.as_view(), name='movie_list'),
    path('movies/create/', MovieCreateView.as_view(), name='movie_create'),
    path('movies/<int:pk>/', MovieRetrieveUpdateDestroytView.as_view(), name='movie_update_delete'),
]