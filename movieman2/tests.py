import datetime

import tmdbsimple as tmdb
from django.contrib.auth.models import User
from django.test import TestCase

from .models import Movie
from .select_movie import (plain_random, rank_order, select_movie,
                           weighted_random)


class MovieTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="movie_test_case", password="pass", email="movie@test_case.tld",
                            first_name="Movie", last_name="TestCase")

    def test_can_create_movie(self):
        """Can movies be created in the database?"""
        movie_data = tmdb.Movies(550).info()
        m = Movie.objects.create(tmdb_id=movie_data["id"], score=10, submitter=User.objects.first(),
                                 title=movie_data["title"], tagline=movie_data["tagline"],
                                 overview=movie_data["overview"],
                                 release_date=datetime.datetime.strptime(movie_data["release_date"], "%Y-%m-%d"),
                                 budget=movie_data["budget"], vote_average=movie_data["vote_average"],
                                 vote_count=movie_data["vote_count"], original_language=movie_data["original_language"])
        m.save()

    def test_can_create_movie_from_id(self):
        """Does Movie.add_from_id work?"""
        Movie.add_from_id(550, User.objects.first())


class MovieSelectionTestCase(TestCase):
    movie_list = None

    def setUp(self):
        User.objects.create(username="movie_selection_test_case", password="pass",
                            email="movie@selection_test_case.tld", first_name="MovieSelection", last_name="TestCase")
        self.movie_list = Movie.objects.all()
        Movie.add_from_id(550, User.objects.first())
        Movie.add_from_id(551, User.objects.first())
        Movie.add_from_id(552, User.objects.first())

    def test_can_select_movie(self):
        select_movie(self.movie_list)

    def test_can_select_movie_plain_random(self):
        select_movie(self.movie_list, selection_method=plain_random)

    def test_can_select_movie_weighted_random(self):
        select_movie(self.movie_list, selection_method=weighted_random)

    def test_can_select_movie_rank_order(self):
        select_movie(self.movie_list, selection_method=rank_order)
