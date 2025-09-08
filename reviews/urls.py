from django.urls import path
from .views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView


urlpatterns = [
    path('reviews/', ReviewCreateListView.as_view(), name='review_list_create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyView.as_view(), name='review_update_delete'),
]