import random


def _select_random(movie_list):
    """Private method for picking a random choice from a list"""
    return random.SystemRandom().choice(movie_list)


def plain_random(movie_list):
    """Select a random movie. No fancy tricks"""
    return _select_random(movie_list)


def rank_order(movie_list):
    """Select movie with the highest score"""
    return movie_list.order_by('-score')[0]  # TODO: Handle multiple #1 spots


def weighted_random(movie_list):
    """Select random movie, but be biased towards movies with higher scores"""
    choices = []
    for movie in movie_list:
        for x in range(0, movie.score):
            choices.append(movie)
    return _select_random(choices)


def select_movie(movie_list, selection_method=plain_random):
    """Selects a movie from the database"""
    return selection_method(movie_list)
