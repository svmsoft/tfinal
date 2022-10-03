from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse
from .models import Clientes
from .models import Material
from .models import Rents
from .models import Tipo
from .models import Usuarios
from t_final.forms import Form_clientes
from t_final.forms import Form_tipo
from t_final.forms import Form_material
from t_final.forms import Form_rents 
from t_final.forms import Form_usuarios
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required

# Create your views here. 
@login_required
#Home
def Principal(request):
    
    return render(request, "index.html")
#-----------------------------------------------------


################ CLIENTES ##########################
#------------------------------------------------------------- OK
      #Nuevo Cliente
#@login_required(login_url='/accounts/login')
@login_required
def N_cliente(request):
    if request.method=="POST":
        miFormulario=Form_clientes(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data
            cliente1 = Clientes(nombre=dataForm.get('nombre'), dni=dataForm.get('dni'), fecha_nac=dataForm.get('fecha_nac'), domicilio=dataForm.get('domicilio'), telefono=dataForm.get('telefono'), activo=dataForm.get('activo'))
            cliente1.save()
            
            
            return render(request, "nuevoregistro.html")
    else:
        miFormulario=Form_clientes()
    return render(request, "n_cliente.html", {"form":miFormulario})

#--------------------------------------------------

#listado clientes (class)
#@login_required(login_url='/accounts/login')
class Clientes_view(ListView):
    model = Clientes
    template_name = 'c_lista.html'
    #paginacion -- tambien hay que poner el codigo en el template
    paginate_by = 10   
    context_object_name = 'clientes'

#-----------------------------------------------------------
    #Listado de clientes

#def C_lista(request):
#    clientes_qset = Clientes.objects.all()
#    contexto = {'clientes' : clientes_qset}
#    return render(request, "c_lista.html", contexto)  

#------------------------------------------------------    
# Editar cliente
#@login_required(login_url='/accounts/login')
def Edit_cliente(request, id):
    cli_edit_qset = Clientes.objects.get(id=id)

    if request.method=="POST":
        miFormulario=Form_clientes(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data

            cli_edit_qset.nombre = dataForm.get('nombre')
            cli_edit_qset.dni = dataForm.get('dni')
            cli_edit_qset.fecha_nac = dataForm.get('fecha_nac')
            cli_edit_qset.domicilio = dataForm.get('domicilio')
            cli_edit_qset.telefono = dataForm.get('telefono')
            cli_edit_qset.activo = dataForm.get('activo')
         

            cli_edit_qset.save()


            
            return render(request, "editar.html")

    contexto = {
        'form' : Form_clientes(
            initial={
                "nombre": cli_edit_qset.nombre,
                "dni": cli_edit_qset.dni,
                "fecha_nac": cli_edit_qset.fecha_nac,
                "domicilio": cli_edit_qset.domicilio,
                "telefono": cli_edit_qset.telefono,
                "activo": cli_edit_qset.activo,
                
            }   
        )
    }
    return render(request, "n_cliente.html", contexto)





################# ALQUILERES ########################

 #Listado de alquileres (reemplazado por la vista de clase Rents_view)

#def A_lista(request):

#    rents = Rents.objects.all()

#    contexto = {'alquileres' : rents}
#    return render(request, "a_lista.html", contexto)    

   #-----------------------------------------------------------

#listado alquileres (class)
#@login_required(login_url='/accounts/login')
class Rents_view(ListView):
    model = Rents
    template_name = 'a_lista.html'
    #paginacion -- tambien hay que poner el codigo en el template
    paginate_by = 10   
    context_object_name = 'alquileres'
#-----------------------------------------------------

#Eliminar Alquiler
#@login_required(login_url='/accounts/login')
def Del_rent(request, id):
    rent_delete = Rents.objects.get(id=id)
    rent_delete.delete()
    return render(request, "eliminar.html")
#---------------------------------------------------------
# Editar Alquiler
#@login_required(login_url='/accounts/login')
def Edit_rent(request, id):
    rent_edit_qset = Rents.objects.get(id=id)

    if request.method=="POST":
        miFormulario=Form_rents(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data

            rent_edit_qset.id_cliente = dataForm.get('id_cliente')
            rent_edit_qset.id_material = dataForm.get('id_material')
            rent_edit_qset.fecha_alq = dataForm.get('fecha_alq')
            rent_edit_qset.hora_alq = dataForm.get('hora_alq')
            rent_edit_qset.fecha_dev_est = dataForm.get('fecha_dev_est')
            rent_edit_qset.hora_dev_est = dataForm.get('hora_dev_est')
            rent_edit_qset.pagado = dataForm.get('pagado')
            rent_edit_qset.importe = dataForm.get('importe')

            rent_edit_qset.save()


            
            return render(request, "editar.html")

    contexto = {
        'form' : Form_rents(
            initial={
                "id_cliente": rent_edit_qset.id_cliente,
                "id_material": rent_edit_qset.id_material,
                "fecha_alq": rent_edit_qset.fecha_alq,
                "hora_alq": rent_edit_qset.hora_alq,
                "fecha_dev_est": rent_edit_qset.fecha_dev_est,
                "hora_dev_est": rent_edit_qset.hora_dev_est,
                "pagado": rent_edit_qset.pagado,
                "importe": rent_edit_qset.importe,
            }   
        )
    }
    return render(request, "n_rent.html", contexto)

#-----------------------------------------------------------
 #Nuevo alquiler
#@login_required(login_url='/accounts/login')
def N_rent(request):
    if request.method=="POST":
        miFormulario=Form_rents(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data
            alquiler1 = Rents(id_cliente=dataForm.get('id_cliente'), id_material=dataForm.get('id_material'), fecha_alq=dataForm.get('fecha_alq'), hora_alq=dataForm.get('hora_alq'), fecha_dev_est=dataForm.get('fecha_dev_est'), hora_dev_est=dataForm.get('hora_dev_est'), pagado=dataForm.get('pagado'), importe=dataForm.get('importe'))
            alquiler1.save()
            return render(request, "nuevoregistro.html")
    else:
        miFormulario=Form_rents()
    return render(request, "n_rent.html", {"form":miFormulario})


#-----------------------------------------------------------
   



















############# DEVOLUCIONES ########################################

    #Devolucion de alquileres
#@login_required(login_url='/accounts/login')
def Devoluciones(request):
    return render(request, "devoluciones.html")

















    ################ MATERIALES #############################

    
    #----------------------------------------------------------- OK
    #Nuevo Material
#@login_required(login_url='/accounts/login')
def N_material(request):
    if request.method=="POST":
        miFormulario=Form_material(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data
            nmaterial1 = Material(codigo=dataForm.get('codigo'), descripcion=dataForm.get('descripcion'), id_tipo=dataForm.get('id_tipo'), activo=dataForm.get('activo'))
            nmaterial1.save()
            return render(request, "nuevoregistro.html")
    else:
        miFormulario=Form_material()
    return render(request, "n_material.html", {"form":miFormulario})


    #--------------------------------------------------------
    #Listado de materiales
#def M_lista(request):
 #   return render(request, "m_lista.html")    


 #-----------------------------------------------------------

#listado materiales (class)
#@login_required(login_url='/accounts/login')
class Materiales_view(ListView):
    model = Material
    template_name = 'm_lista.html'
    #paginacion -- tambien hay que poner el codigo en el template
    paginate_by = 10   
    context_object_name = 'materiales'
#--------------------------------------------------

# Editar Material
#@login_required(login_url='/accounts/login')
def Edit_material(request, id):
    materiales_qset = Material.objects.get(id=id)

    if request.method=="POST":
        miFormulario=Form_material(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data

            materiales_qset.codigo = dataForm.get('codigo')
            materiales_qset.descripcion = dataForm.get('descripcion')
            materiales_qset.id_tipo = dataForm.get('id_tipo')
            materiales_qset.activo = dataForm.get('activo')
            
         

            materiales_qset.save()


            
            return render(request, "editar.html")

    contexto = {
        'form' : Form_material(
            initial={
                "codigo": materiales_qset.codigo,
                "descripcion": materiales_qset.descripcion,
                "id_tipo": materiales_qset.id_tipo,
                "activo": materiales_qset.activo,
                
            }   
        )
    }
    return render(request, "n_material.html", contexto)











#################### TIPOS DE MATERIALES #######################


    #--------------------------------------------------------- OK
    #Nuevo tipo de material
#@login_required(login_url='/accounts/login')
def N_tipo(request):
    if request.method=="POST":
        miFormulario=Form_tipo(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data
            ntipo1 = Tipo(nombre=dataForm.get('nombre'), activo=dataForm.get('activo'))
            ntipo1.save()
            
            return render(request, "nuevoregistro.html")
    else:
        miFormulario=Form_tipo()
    return render(request, "n_tipo.html", {"form":miFormulario}) 

    #---------------------------------------------------------------
    #Listado de tipos de materiales
#def T_lista(request):

 #   return render(request, "t_lista.html")

#-----------------------------------------------------------

#listado tipos materiales (class)
#@login_required(login_url='/accounts/login')
class Tmateriales_view(ListView):
    model = Tipo
    template_name = 't_lista.html'
    #paginacion -- tambien hay que poner el codigo en el template
    paginate_by = 10   
    context_object_name = 'tipos'
#--------------------------------------------------

# Editar Tipo Material
#@login_required(login_url='/accounts/login')
def Edit_tmaterial(request, id):
    tmateriales_qset = Tipo.objects.get(id=id)

    if request.method=="POST":
        miFormulario=Form_tipo(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data

            tmateriales_qset.nombre = dataForm.get('nombre')
          
            tmateriales_qset.activo = dataForm.get('activo')
            
         

            tmateriales_qset.save()


            
            return render(request, "editar.html")

    contexto = {
        'form' : Form_tipo(
            initial={
                "nombre": tmateriales_qset.nombre,
                
                "activo": tmateriales_qset.activo,
                
            }   
        )
    }
    return render(request, "n_tipo.html", contexto)


    ###################### usuarios #####################

    #EDITAR USUARIO------------------------

#@login_required(login_url='/accounts/login')
def Edit_usuario(request, id):

    usuario_qset = Usuarios.objects.get(id=id)

    if request.method=="POST":
        miFormulario=Form_usuarios(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data

            usuario_qset.nombre = dataForm.get('nombre')
            usuario_qset.clave = dataForm.get('clave')
            usuario_qset.permiso = dataForm.get('permiso')
            usuario_qset.activo = dataForm.get('activo')
            
         

            usuario_qset.save()


            
            return render(request, "editar.html")

    contexto = {
        'form' : Form_usuarios(
            initial={
                "nombre": usuario_qset.nombre,
                "clave": usuario_qset.clave,
                "permiso": usuario_qset.permiso,
                "activo": usuario_qset.activo,
                
            }   
        )
    }
    return render(request, "n_usuario.html", contexto)
    
   #-----------------------------------------------------------

#listado usuarios (class)
#@login_required(login_url='/accounts/login')
class Usuarios_view(ListView):
    model = Usuarios
    template_name = 'u_lista.html'     
    
  #--------------------------------------------------------- OK
    #Nuevo Usuario
#@login_required(login_url='/accounts/login')
def N_usuario(request):
    if request.method=="POST":
        miFormulario=Form_usuarios(request.POST)
        if miFormulario.is_valid():
            dataForm=miFormulario.cleaned_data
            usuario1 = Usuarios(nombre=dataForm.get('nombre'), clave=dataForm.get('clave'), permiso=dataForm.get('permiso'), activo=dataForm.get('activo'))
            usuario1.save()
            
            return render(request, "nuevoregistro.html")
    else:
        miFormulario=Form_usuarios()
    return render(request, "n_usuario.html", {"form":miFormulario})    
    
    
    
    
    
    
    
    
    
    

#def principal(request):
#   nombre = miembros.objects.create(nombre = "Jorge",saldo = 1000000, fecha_nac = "1958-09-05")
#   context = {'miembro':miembros}


#   return render(request, 'principal.html', context={})

#def lista(request):
#     miembro= miembros.objects.all()
#    context = {'array': miembro}
#     return render(request, "lista.html", context={})