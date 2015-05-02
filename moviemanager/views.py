from django.shortcuts import render_to_response
import tmdbsimple as tmdb


def add_movies(request, movie_title):
    search = tmdb.Search()
    response = search.movie(query=movie_title)
    dictionary = {
        "movies": search.results
    }
    return render_to_response("moviemanager/add_movies.html", dictionary=dictionary)