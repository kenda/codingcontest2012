from tastypie.resources import ModelResource
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization

from books.models import Autor, Buch, Genre, Sammlung, Tag, Verlag

class AutorResource(ModelResource):
    class Meta:
        queryset = Autor.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

class BuchResource(ModelResource):
    class Meta:
        queryset = Buch.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

class GenreResource(ModelResource):
    class Meta:
        queryset = Genre.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

class SammlungResource(ModelResource):
    class Meta:
        queryset = Sammlung.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

        
class TagResource(ModelResource):
    class Meta:
        queryset = Tag.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()

class VerlagResource(ModelResource):
    class Meta:
        queryset = Verlag.objects.all()
        allowed_methods = ['get', 'post', 'put', 'delete']
        authentication = BasicAuthentication()
        authorization = DjangoAuthorization()
