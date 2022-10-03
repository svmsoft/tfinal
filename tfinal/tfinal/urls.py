"""tfinal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from t_final.views import Principal
from t_final.views import N_rent
from t_final.views import Rents_view
from t_final.views import Devoluciones
from t_final.views import N_cliente
#from t_final.views import C_lista
from t_final.views import N_material
#from t_final.views import M_lista
from t_final.views import N_tipo
#from t_final.views import T_lista
from t_final.views import Del_rent
from t_final.views import Edit_rent
from t_final.views import Clientes_view
from t_final.views import Edit_cliente
from t_final.views import Edit_material
from t_final.views import Materiales_view
from t_final.views import Tmateriales_view
from t_final.views import Edit_tmaterial
from t_final.views import N_usuario
from t_final.views import Edit_usuario
from t_final.views import Usuarios_view
from django.contrib.auth import login

urlpatterns = [
    #path('/', lambda req: redirect('Principal')),
    #protector de url's
    #path('accounts/login/', auth_views.LoginView.as_view()),
    #path('accounts/', include('django.contrib.auth.urls')),
    #ath('accounts/', include('django.contrib.auth.urls')),

    path('', Principal),
    #path('', include('app.urls')),
    path('admin/', admin.site.urls),
    #login
    path('login/', login, {'template_name':'login.html'}, name='url_login'),
    #home
    path('principal/',Principal, name='url_Principal'),


    ########### ALQUILERES ##################
    
    #Nuevo alquiler
    path('n_alquiler/',N_rent, name='url_N_alquiler'),

    #Lista de alquileres (class)
    path('a_lista/',Rents_view.as_view(), name='url_A_lista'),

    #Eliminación de alquileres
    path('rent_del/<int:id>',Del_rent, name='url_rent_del'),
    
    #Edición de alquileres
    path('rent_edit/<int:id>', Edit_rent, name='url_rent_edit'),
    
    ############## DEVOLUCIONES ###############
    
    #Devoluciones
    path('devoluciones/',Devoluciones, name='url_Devoluciones'),

    ############## CLIENTES ##################
    
    #Nuevo Cliente
    path('n_cliente/',N_cliente, name='url_N_cliente'),
    
    #Lista de clientes
    #path('c_lista/',C_lista, name='url_C_lista'),

    #Lista de clientes (class)
    path('c_lista/',Clientes_view.as_view(), name='url_C_lista'),

    #Edición de clientes
    path('cli_edit/<int:id>', Edit_cliente, name='url_cli_edit'),

    ########### MATERIALES ##################

    #Nuevo Material
    path('n_material/',N_material, name='url_N_material'),
    
    #Lista de Materiales
    path('m_lista/',Materiales_view.as_view(), name='url_M_lista'),


    #Edicion de materiales
    path('materiales_edit/<int:id>', Edit_material, name='url_m_edit'),


    ######### TIPOS DE MATERIALES ################
    
    #Nuevo Tipo de material
    path('tipos/',N_tipo, name='url_N_tipos'),
    
    #Lista de tipos de material
    #path('t_lista/',T_lista, name='url_T_lista'),
    
    
    #Lista de Tipos Materiales
    path('t_lista/',Tmateriales_view.as_view(), name='url_T_lista'),
    
    #Edicion de tipo materiales
    path('tmateriales_edit/<int:id>', Edit_tmaterial, name='url_tm_edit'),


######### USUARIOS ################
    
    #Nuevo usuario
    path('usuarios/',N_usuario, name='url_N_usuario'),
    
    #Lista usuarios
    #path('t_lista/',T_lista, name='url_T_lista'),
    
    
    #Lista usuarios
    path('t_usuarios/',Usuarios_view.as_view(), name='url_u_lista'),
    
    #Edicion usuarios
    path('usuarios_edit/<int:id>', Edit_usuario, name='url_u_edit'),

]