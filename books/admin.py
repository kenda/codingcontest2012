# -*- coding: utf-8 -*-
from books.models import Autor, Buch, Genre, Sammlung, Tag, Verlag
from django.contrib import admin

# Registrierung der einzelnen Module für das Admin-Interface
admin.site.register(Autor)
admin.site.register(Buch)
admin.site.register(Genre)
admin.site.register(Sammlung)
admin.site.register(Tag)
admin.site.register(Verlag)
