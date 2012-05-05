from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext

from books.forms import BuchForm
from books.models import Buch

def index(request):
    #latest_poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    return render_to_response('index.html',{}, context_instance=RequestContext(request))

def add_buch(request):
    if request.method == 'POST':
        addForm = BuchForm(request.POST)
        if addForm.is_valid():
            addForm.save()
            return redirect(index)
    else:
        addForm = BuchForm()

    return render_to_response('add.html', {'form': addForm, }, context_instance = RequestContext( request ) )

def edit_buch( request, id ):
    buch = get_object_or_404(Buch, pk=id)
    if request.method == 'POST':
        editForm = BuchForm(request.POST, instance=buch)
        if editForm.is_valid():
            editForm.save()
            return redirect(index)
    else:
        editForm = BuchForm(instance=buch)
    return render_to_response('add.html', {'id': id, 'form': editForm}, context_instance = RequestContext( request ) ) 

def del_buch( request, id ):
    Buch.objects.get(pk=id).delete()
    return redirect(index)
