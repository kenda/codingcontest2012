# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms.fields import DateField, ChoiceField, IntegerField, CharField
from django.forms.widgets import RadioSelect, CheckboxSelectMultiple, Select, TextInput
from django.forms.extras.widgets import SelectDateWidget

from books.models import Buch


class BuchForm(ModelForm):
    """
    Formular für das Anlegen und Ändern von Buch-Instanzen.
    """
    titel = CharField(widget=TextInput(attrs={'size':'50'}))
    bewertung = ChoiceField(widget=Select, choices=(
            (1, "1"),
            (2, "2"),
            (3, "3"),
            (4, "4"),
            (5, "5")
            ))
    veroeffentlichung = DateField(widget=SelectDateWidget())
    preis = CharField(widget=TextInput(attrs={'size':'10'}))
    lesezeichen = IntegerField(widget=TextInput(attrs={'size':'10'}))
    
    class Meta:
        model = Buch
