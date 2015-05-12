from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^add_movies/(?P<movie_title>.*)$', views.add_movies, name="add_movies"),
    url(r'^list_saved_movies$', views.list_saved_movies, name="list_saved_movies"),
    url(r'^show_movie/(?P<movie_id>\d*)', views.show_movie, name="show_movie"),
)
