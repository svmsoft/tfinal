from multiprocessing import context
from django.shortcuts import render
from django.http import HttpReponse
from t_final.forms import Form_clientes
from t_final.forms import Form_tipo
from t_final.forms import Form_material
from t_final.forms import Form_rents 


# Create your views here. 
def clientes(request):
    if request.metod=="POST":
        miFormulario=Form_clientes(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data
            
            return render(request, "nuevoregistro.html")
    else:
        miFormulario=Form_clientes()
    return render(request, "n_cliente.html")

def principal(request):
   nombre = miembros.objects.create(nombre = "Jorge",saldo = 1000000, fecha_nac = "1958-09-05")
   context = {'miembro':miembros}


   return render(request, 'principal.html', context={})

def lista(request):
     miembro= miembros.objects.all()
     context = {'array': miembro}
     return render(request, "lista.html", context={})