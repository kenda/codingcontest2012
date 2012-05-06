# -*- coding: utf-8 -*-
"""
Dieses Modul stellt die jeweiligen Resourcen zu den Models als
REST-Schnittstelle zur Verfügung.

Dabei sind standardmäßig alle Operationen (get, post, put, delete)
erlaubt. Es finden keine Einschränkungne bei den Queries statt -
es werden immer alle verfügbaren Daten geliefert.

Die Authentifizierung findet über HTTP Basic mit den Django-Logindaten
statt.

Buch-Objekte werden voll aufgelößt, d.h. es werden bspw. bei
ForeignKey-Feldern ganze Objekte statt Referenzen zurückgegeben.
"""
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization
from tastypie import fields
from tastypie.resources import ModelResource, ALL

from books.models import Autor, Buch, Genre, Sammlung, Tag, Verlag


class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        resource_name = 'autor'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        resource_name = 'genre'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class SammlungResource(ModelResource):
    class Meta:
        queryset = Sammlung.objects.all()
        resource_name = 'sammlung'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()
        filtering = {
            'id': ALL,
        }


class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        resource_name = 'tag'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class VerlagResource(ModelResource):
    class Meta:
        queryset = Verlag.objects.all()
        resource_name = 'verlag'
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class BuchResource(ModelResource):
    sammlung = fields.ForeignKey(SammlungResource, "sammlung", full=True, null=True)
    verlag = fields.ForeignKey(VerlagResource, "verlag", full=True, null=True)
    autor = fields.ToManyField(AutorResource, 'autor', full=True)
    genre = fields.ToManyField(GenreResource, 'genre', full=True)
    tag = fields.ToManyField(TagResource, 'tag', full=True)
    
    class Meta:
        queryset = Buch.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()
        filtering = {
            'sammlung': ALL,
        }



