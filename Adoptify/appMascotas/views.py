from django.shortcuts import render
from appMascotas.models import Publicacion

# Create your views here.

def publicacion(request):
    publicaciones = Publicacion.objects.all()
    return render(request,
                  'index.html', {'publicaciones': publicaciones})
    #              {'cuentas': cuentas,
    #               'total': total}
