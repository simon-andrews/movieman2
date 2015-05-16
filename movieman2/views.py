import tmdbsimple as tmdb
from django.shortcuts import redirect, render_to_response

from .models import Movie
from .select_movie import weighted_random


def index(request):
    return redirect(list_saved_movies)


def add_movies(request, movie_title):
    search = tmdb.Search()
    search.movie(query=movie_title, include_adult=True)
    dictionary = {
        "movies": search.results
    }
    return render_to_response("moviemanager/add_movies.html", dictionary=dictionary)


def list_saved_movies(request):
    # TODO: Paginator
    dictionary = {
        "movies": Movie.objects.all()
    }
    return render_to_response("moviemanager/list_saved_movies.html", dictionary=dictionary)


def show_movie(request, movie_id):
    movie_data = tmdb.Movies(movie_id).info()
    dictionary = {
        "movie": movie_data,
    }
    return render_to_response("moviemanager/movie.html", dictionary=dictionary)


def random_movie(request):
    movie = weighted_random(Movie.objects.all())
    movie_data = tmdb.Movies(movie.tmdb_id).info()
    dictionary = {
        "movie": movie_data
    }
    return render_to_response("moviemanager/movie.html", dictionary=dictionary)
