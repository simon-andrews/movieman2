from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    tmdb_id = models.IntegerField()
    score = models.IntegerField()
    submitter = models.ForeignKey(User)