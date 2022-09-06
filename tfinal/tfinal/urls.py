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
from django.urls import path
from t_final.views import Principal
from t_final.views import N_alquiler
from t_final.views import A_lista
from t_final.views import Devoluciones
from t_final.views import N_cliente
from t_final.views import C_lista
from t_final.views import N_material
from t_final.views import M_lista
from t_final.views import N_tipos
from t_final.views import T_lista

urlpatterns = [
    path('/', lambda req: redirect('Principal')),
    path('admin/', admin.site.urls),
    path('principal/',Principal, name='url_Principal'),
    path('n_alquiler/',N_alquiler, name='url_N_alquiler'),
    path('a_lista/',A_lista, name='url_A_lista'),
    path('devoluciones/',Devoluciones, name='url_Devoluciones'),
    path('n_cliente/',N_cliente, name='url_N_cliente'),
    path('c_lista/',C_lista, name='url_C_lista'),
    path('n_material/',N_material, name='url_N_material'),
    path('m_lista/',M_lista, name='url_M_lista'),
    path('tipos/',N_tipos, name='url_N_tipos'),
    path('t_lista/',T_lista, name='url_T_lista'),
]