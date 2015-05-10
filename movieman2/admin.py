from django.contrib import admin

from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'score',
        'submitter',
        'release_date',
        'tmdb_id'
    )

# Register your models here.
admin.site.register(Movie, MovieAdmin)
