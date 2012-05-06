# -*- coding: utf-8 -*-
from django.forms import ModelForm

from books.models import Buch


class BuchForm(ModelForm):
    """
    Formular für das Anlegen und Ändern von Buch-Instanzen.
    """
    class Meta:
        model = Buch
