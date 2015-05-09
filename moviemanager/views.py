from django.shortcuts import render_to_response
from .models import Movie
import tmdbsimple as tmdb


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
