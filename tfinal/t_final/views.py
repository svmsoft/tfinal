from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Clientes
from .models import Material
from .models import Rents
from .models import Tipo
from t_final.forms import Form_clientes
from t_final.forms import Form_tipo
from t_final.forms import Form_material
from t_final.forms import Form_rents 


# Create your views here. 


def Principal(request):
    return render(request, "index.html")

def N_rent(request):
    return render(request, "n_rent.html")

def A_lista(request):
    return render(request, "a_lista.html")    

def Devoluciones(request):
    return render(request, "devoluciones.html")

def C_lista(request):
    return render(request, "c_lista.html")  

def N_material(request):
    return render(request, "n_material.html")

def M_lista(request):
    return render(request, "m_lista.html")    
    
def N_tipo(request):
    return render(request, "n_tipo.html") 
    
def T_lista(request):
    return render(request, "t_lista.html")

def N_cliente(request):
    if request.metod=="POST":
        miFormulario=Form_clientes(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data
            
            return render(request, "nuevoregistro.html")
    else:
        miFormulario=Form_clientes()
    return render(request, "N_cliente.html", {"form":miFormulario})
    
    
    
    
    
    
    
    
    
    
    
    
    

#def principal(request):
#   nombre = miembros.objects.create(nombre = "Jorge",saldo = 1000000, fecha_nac = "1958-09-05")
#   context = {'miembro':miembros}


#   return render(request, 'principal.html', context={})

#def lista(request):
#     miembro= miembros.objects.all()
#    context = {'array': miembro}
#     return render(request, "lista.html", context={})