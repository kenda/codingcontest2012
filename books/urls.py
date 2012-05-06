from django.conf.urls import patterns, include, url

# URL-Config des book-Moduls
urlpatterns = patterns('books.views',
                       url('^add/$', 'add_buch'),
                       url(r'^(?P<id>\d+)/$', 'view_buch'),
                       url(r'^edit/(?P<id>\d+)/$', 'edit_buch'),
                       url(r'^del/(?P<id>\d+)/$', 'del_buch')
                       )

# statische HTML-Seite als Startseite ausliefern
urlpatterns += patterns('django.views.generic.simple',
                        (r'^$', 'direct_to_template', {'template': 'index.html'}),
)
