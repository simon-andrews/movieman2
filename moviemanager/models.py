from django.contrib.auth.models import User
from django.db import models
import tmdbsimple as tmdb
import datetime


class Movie(models.Model):
    # General
    tmdb_id = models.IntegerField()
    score = models.IntegerField()
    submitter = models.ForeignKey(User)

    # Movie metadata
    title = models.CharField(max_length=128)
    tagline = models.TextField()
    overview = models.TextField()
    release_date = models.DateField()
    budget = models.IntegerField()
    vote_average = models.DecimalField(max_digits=2, decimal_places=1)
    vote_count = models.IntegerField()
    original_language = models.CharField(max_length=2)

    @staticmethod
    def add_from_id(tmdb_id, submitter):
        movie_data = tmdb.Movies(tmdb_id).info()
        m = Movie.objects.create(tmdb_id=movie_data["id"], score=10, submitter=submitter, title=movie_data["title"],
                                 tagline=movie_data["tagline"], overview=movie_data["overview"],
                                 release_date=datetime.datetime.strptime(movie_data["release_date"], "%Y-%m-%d"),
                                 budget=movie_data["budget"], vote_average=movie_data["vote_average"],
                                 vote_count=movie_data["vote_count"], original_language=movie_data["original_language"])
        m.save()
