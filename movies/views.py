from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from movies.models import Movie
from .forms import NameForm
from django.contrib.auth import authenticate, login, logout
from .forms import MovieReviewForm
from django.shortcuts import render, get_object_or_404
from django.db.models import Avg

# Create your views here.


def index(request):
    movies = Movie.objects.all()
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
    
def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print(form.cleaned_data)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, "name_ok.html", {"form": form})
        else:
            return render(request, "name_ok.html", {"form": form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, "name.html", {"form": form})
    
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))
   

