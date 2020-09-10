from django.shortcuts import render, redirect
from appMascotas.models import Publicacion
from appMascotas.forms import *
# Create your views here.

def index(request):
    publicaciones = Publicacion.objects.all()
    return render(request,
                  'index.html', {'publicaciones': publicaciones})




def crear(request):                
    if request.method=='POST':
        form=PublicacionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form=PublicacionForm()
        return render(request,'nuevPu.html',{'form':form})


def publicacion(request, id):
    try:
        publicacion = Publicacion.objects.get(pk=id)
    except Publicacion.DoesNotExist:
        raise Http404("La cuenta no existe")

    return render(request,
                  'publicacion.html',
                  {'publicacion': publicacion})