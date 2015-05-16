import datetime

from django.contrib.auth.models import User
from django.test import TestCase

import tmdbsimple as tmdb
from .models import Movie


class MovieTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test_user", password="pass", email="test@user.tld", first_name="Test",
                            last_name="User")

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
