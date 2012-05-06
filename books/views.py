# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from books.forms import BuchForm
from books.models import Buch


def add_buch(request):
    """
    Funktion zum Hinzufügen eines Buches.

    Testet jeweils ob der Aufruf als POST oder GET
    abegesetzt wurde und liefert je nach dem das
    Ausgangsformular aus oder legt ein neues Buch an.
    """
    if request.method == 'POST':
        addForm = BuchForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            return redirect("/")
    else:
        addForm = BuchForm()

    return render_to_response('addedit.html',
                              {'form': addForm, },
                              context_instance=RequestContext(request))


def edit_buch(request, id):
    """
    Funktion zum Bearbeiten einer Buch-Instanz.

    Verfährt beim Bearbeiten wie add_buch().
    """
    buch = get_object_or_404(Buch, pk=id)
    if request.method == 'POST':
        editForm = BuchForm(request.POST, instance=buch)
        if editForm.is_valid():
            editForm.save()
            return redirect("/")
    else:
        editForm = BuchForm(instance=buch)
    return render_to_response('addedit.html', {'id': id,
                                               'buch': buch,
                                               'form': editForm},
                              context_instance=RequestContext(request)) 


def del_buch(request, id):
    """
    Funktion zum Löschen einer Buch-Instanz.
    """
    Buch.objects.get(pk=id).delete()
    return redirect("/")


def view_buch(request, id):
    """
    Funktion zum Ausliefern aller Details einer Buch-Instanz.

    Es werden hierbei alle referenzierten Felder aufgelößt und
    an das Template weitergeleitet.
    """
    buch = get_object_or_404(Buch, pk=id)
    autoren = buch.autor.all()
    tags = buch.tag.all()
    genre = buch.genre.all()
    return render_to_response('details.html',
                              {'id': id,
                               'buch': buch,
                               'autoren': autoren,
                               'tags': tags,
                               'genre': genre},
                              context_instance=RequestContext(request))
