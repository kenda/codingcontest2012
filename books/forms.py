from django.forms import ModelForm

from books.models import Buch


class BuchForm(ModelForm):
    class Meta:
        model = Buch
