from django.contrib.auth.models import User
from django.test import TestCase
from .models import Movie
import datetime

movie_data = {
    "adult": False,
    "backdrop_path": "/hNFMawyNDWZKKHU4GYCBz1krsRM.jpg",
    "belongs_to_collection": None,
    "budget": 63000000,
    "genres": [
        {
            "id": 18,
            "name": "Drama"
        }
    ],
    "homepage": "",
    "id": 550,
    "imdb_id": "tt0137523",
    "original_language": "en",
    "original_title": "Fight Club",
    "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a"
                "shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in"
                "every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
    "popularity": 2.50307202280779,
    "poster_path": "/2lECpi35Hnbpa4y46JX0aY3AWTy.jpg",
    "production_companies": [
        {
            "name": "20th Century Fox",
            "id": 25
        },
        {
            "name": "Fox 2000 Pictures",
            "id": 711
        },
        {
            "name": "Regency Enterprises",
            "id": 508
        }
    ],
    "production_countries": [
        {
            "iso_3166_1": "DE",
            "name": "Germany"
        },
        {
            "iso_3166_1": "US",
            "name": "United States of America"
        }
    ],
    "release_date": "1999-10-14",
    "revenue": 100853753,
    "runtime": 139,
    "spoken_languages": [
        {
            "iso_639_1": "en",
            "name": "English"
        }
    ],
    "status": "Released",
    "tagline": "How much can you know about yourself if you've never been in a fight?",
    "title": "Fight Club",
    "video": False,
    "vote_average": 7.7,
    "vote_count": 3185
}


class MovieTestCase(TestCase):
    def setUp(self):
        User.objects.create(username="test_user", password="pass", email="test@user.tld", first_name="Test",
                            last_name="User")

    def test_can_create_movie(self):
        """Can movies be created in the database?"""
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
