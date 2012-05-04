from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from tastypie.api import Api
from books.api.resources import AutorResource, BuchResource, GenreResource, SammlungResource, TagResource, VerlagResource

v1_api = Api(api_name='v1')
v1_api.register(AutorResource())
v1_api.register(BuchResource())
v1_api.register(GenreResource())
v1_api.register(TagResource())
v1_api.register(VerlagResource())
v1_api.register(SammlungResource())

urlpatterns = patterns('',
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

    (r'^api/', include(v1_api.urls)),
)
