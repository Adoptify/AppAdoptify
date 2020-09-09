from django.shortcuts import render
from appMascotas import models

# Create your views here.

def publicacion(request):
 #   publicacion = Publicacion.objects.all()
    return render(request,
                  'index.html')
    #              {'cuentas': cuentas,
    #               'total': total}
                   



