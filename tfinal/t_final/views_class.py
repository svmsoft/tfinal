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
from django.views.generic import List
View



# Create your views here. 

class Rents_view(ListView):
	model = Rents
	template_name = 'a_lista.html'