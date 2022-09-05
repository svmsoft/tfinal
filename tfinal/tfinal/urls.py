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
from t_final.views import principal
from t_final.views import n_alquiler
from t_final.views import a_lista
from t_final.views import devoluciones
from t_final.views import n_cliente
from t_final.views import c_lista
from t_final.views import n_material
from t_final.views import m_lista
from t_final.views import tipos
from t_final.views import t_lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/',principal),
    path('n_alquiler/',n_alquiler),
    path('a_lista/',a_lista),
    path('devoluciones/',devoluciones),
    path('n_cliente',n_cliente),
    path('c_lista/',c_lista),
    path('n_material/',n_material),
    path('m_lista/',m_lista),
    path('a_lista/',a_lista),
    path('tipos/',tipos),
    path('t_lista/',t_lista),
]