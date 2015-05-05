from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^addmovies/(?P<movie_title>.*)$', views.add_movies, name="add_movies"),
)
