from django.conf.urls import patterns, include, url

urlpatterns = patterns('books.views',
                       url('^$', 'index'),
                       url('^add/$', 'add_buch'),
                       url(r'^(?P<id>\d+)/$', 'edit_buch'),
                       url(r'^del/(?P<id>\d+)/$', 'del_buch')
                       )
