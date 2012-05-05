from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api

from books.api.resources import AutorResource, BuchResource, GenreResource, SammlungResource, TagResource, VerlagResource

# Registrierung der einzelnen REST-Resourcen
v1_api = Api(api_name='v1')
v1_api.register(AutorResource())
v1_api.register(BuchResource())
v1_api.register(GenreResource())
v1_api.register(SammlungResource())
v1_api.register(TagResource())
v1_api.register(VerlagResource())

urlpatterns = patterns('',
    # Admin-Interface
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    # URL der REST-Schnittstelle
    (r'^api/', include(v1_api.urls)),

    # Books-App einbinden
    url(r'^', include('books.urls')),
)

urlpatterns += staticfiles_urlpatterns()
