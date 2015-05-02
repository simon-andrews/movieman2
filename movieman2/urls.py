from django.conf.urls import include, url
from django.contrib import admin

from moviemanager import urls as moviemanager_urls

urlpatterns = [
    # Examples:
    # url(r'^$', 'movieman2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^movieman/', include(moviemanager_urls))
]
