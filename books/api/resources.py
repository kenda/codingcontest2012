# -*- coding: utf-8 -*-
"""
Dieses Modul stellt die jeweiligen Resourcen zu den Models
als REST-Schnittstelle zur Verfügung.
Dabei sind standardmäßig alle Operationen (get, post, put,
delete) erlaubt. Es finden keine Einschränkungne bei den
Queries statt - es werden immer alle verfügbaren Daten geliefert.
Die Authentifizierung findet über HTTP Basic mit den Django-Logindaten
statt.
"""
from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication, ApiKeyAuthentication, MultiAuthentication
from tastypie.authorization import DjangoAuthorization

from books.models import Autor, Buch, Genre, Sammlung, Tag, Verlag


class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class BuchResource(ModelResource):
    class Meta:
        queryset = Buch.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class SammlungResource(ModelResource):
    class Meta:
        queryset = Sammlung.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()


class VerlagResource(ModelResource):
    class Meta:
        queryset = Verlag.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = MultiAuthentication(BasicAuthentication(), ApiKeyAuthentication())
        authorization = DjangoAuthorization()
