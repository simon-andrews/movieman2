from django.contrib.auth.models import User
from django.db import models


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