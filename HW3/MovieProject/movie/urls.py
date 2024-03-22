from django.urls import path
from .views import MovieListCreateView, MovieDetailView, UserListCreateView, UserDetailView

urlpatterns = [
    path('movies/',MovieListCreateView.as_view(),name = 'movie-list-create'),
    path('movies/<int:pk>/', MovieDetailView.as_view(), name = 'movie-detail'),

    path('users/',UserListCreateView.as_view(),name = 'user-list-create'),
    path('users/<int:pk>/', UserDetailView.as_view(), name = 'user-detail')

]