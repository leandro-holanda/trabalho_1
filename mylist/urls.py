from django.urls import path
from .views import MyListCreateListView, MyListRetrieveUpdateDestroyView


urlpatterns = [
    path('mylist/', MyListCreateListView.as_view(), name='mylist_create_list'),
    path('mylist/<int:pk>/', MyListRetrieveUpdateDestroyView.as_view(), name='name_update_delete'),
]