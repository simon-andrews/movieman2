import random


def plain_random(movie_list):
    return random.SystemRandom().choice(movie_list)


def rank_order(movie_list):
    return movie_list.order_by('-score')[0]  # TODO: Handle multiple #1 spots


def weighted_random(movie_list):
    pass  # TODO: implement


def select_movie(movie_list, selection_method=plain_random):
    """Selects a movie from the database"""
    return selection_method(movie_list)
