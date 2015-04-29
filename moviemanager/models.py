from django.db import models


class Movie(models.Model):
    tmdb_id = models.IntegerField()