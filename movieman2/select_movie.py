import random


def select_movie(movie_list):
    """Selects a movie from the database"""
    return random.SystemRandom().choice(movie_list)
