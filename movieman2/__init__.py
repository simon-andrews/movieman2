import os
import tmdbsimple
from django.conf import settings

tmdbsimple.API_KEY = os.environ['MM2_TMDB_API_KEY'] or settings.MM2_TMDB_API_KEY
