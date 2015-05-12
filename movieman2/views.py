import tmdbsimple as tmdb
from django.shortcuts import render_to_response

from .models import Movie


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
