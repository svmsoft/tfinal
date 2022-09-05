from multiprocessing import context
from django.shortcuts import render

# Create your views here. VISTAS DE MIPRIMER MVT
def principal(request):
   nombre = miembros.objects.create(nombre = "Jorge",saldo = 1000000, fecha_nac = "1958-09-05")
   context = {'miembro':miembros}


   return render(request, 'principal.html', context={})

def lista(request):
     miembro= miembros.objects.all()
     context = {'array': miembro}
     return render(request, "lista.html", context={})