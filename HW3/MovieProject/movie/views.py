from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from rest_framework import generics
from .models import Movie,User
from .serializers import MovieSerializer,UserSerializer
from .forms import MovieForm, UserForm

class MovieList(View):

    def get(self,request):

        movies = Movie.objects.all()

        return render(request = request,
                      template_name = 'movie/movie_list.html',
                      context = {'movies':movies})
    
class MovieEdit(View):

    def get(self,request,movie_id):

        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(instance=movie)

        return render(request = request,
                      template_name = 'movie/movie_edit.html',
                      context = {'movie':movie,'form':form})
    
    def post(self,request,movie_id):

        movie = Movie.objects.get(pk=movie_id)
        form = MovieForm(request.POST,instance=movie)

        if form.is_valid():
            movie = form.save()
        
        return render(request = request,
                      template_name = 'movie/movie_edit.html',
                      context = {'movie':movie,'form':form})
    









class MovieListCreateView(generics.ListCreateAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class MovieDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    