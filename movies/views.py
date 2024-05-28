from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from movies.models import Movie #import
from .forms import LoginForm #import
from django.shortcuts import render, redirect #import
from django.contrib.auth import authenticate, login, logout
from .forms import MovieReviewForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg
from django.db import models
from django.views.generic import ListView
from django.urls import reverse #import


# Create your views here.


def index(request):
    movies = Movie.objects.all().order_by('-release_date')
    context = {'movie_list': movies}
    return render(request, "index.html", context=context)


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            # Guardar el formulario en la base de datos
            review = form.save(commit=False)
            review.movie = movie
            review.user = request.user  # Asignar el usuario actual
            review.save()
            return HttpResponseRedirect(request.path)  # Redirigir a la misma página después de guardar
    else:
        form = MovieReviewForm()

    # Obtener todas las revisiones de la película
    reviews = movie.moviereview_set.all()

    
    # Calcular el promedio de las calificaciones
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    
    context = {'movie': movie, 'form': form, 'average_rating': average_rating}
    return render(request, 'movie_detail.html', context)
    
def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirige a la página de inicio después de iniciar sesión exitosamente
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    