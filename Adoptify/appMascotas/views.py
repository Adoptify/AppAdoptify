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