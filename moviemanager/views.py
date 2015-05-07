from django.shortcuts import render_to_response
import tmdbsimple as tmdb


def add_movies(request, movie_title):
    search = tmdb.Search()
    search.movie(query=movie_title, include_adult=True)
    dictionary = {
        "movies": search.results
    }
    return render_to_response("moviemanager/movie_list.html", dictionary=dictionary)
