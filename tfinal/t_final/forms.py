from django import forms
from django.contrib.admin import widgets
from t_final.models import Tipo
from t_final.models import Clientes
from t_final.models import Material
from t_final.models import Rents
from t_final.models import Usuarios
#from t_final.widgets import DatePickerInput, TimePickerInput, DateTimePickerInput

   #class ExampleForm(forms.Form):
    #    my_date_field = forms.DateField(widget=DatePickerInput)
     #   my_time_field = forms.TimeField(widget=TimePickerInput)
      #  my_date_time_field = forms.DateTimeField(widget=DateTimePickerInput)
#no me gustó el APIForm, volví al otro
#class Form_clientes(forms.Form):
#    nombre=forms.CharField()
#    dni=forms.CharField()
#    fecha_nac=forms.DateField(input_formats=['%d/%m/%Y'])
#    domicilio=forms.CharField()
#    telefono=forms.CharField()

### CLASE PARA EL CALENDARIO#######
class DateInput(forms.DateInput):
    input_type = 'date'
class TimeInput(forms.DateInput):
    input_type = 'time'    

#########################################################
class Form_clientes(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = [
            'nombre',
            'dni',
            'fecha_nac',
            'domicilio',
            'telefono',
            'activo',
        ]
        labels = {
            'nombre':'Nombre',
            'dni':'DNI',
            'fecha_nac':'Fecha de nacimiento',
            'domicilio':'Domicilio',
            'telefono':'Teléfono',
            'activo' : 'Activo',
        }
        Opcion = ['SS','NN']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'dni': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_nac': DateInput(),
            'domicilio': forms.TextInput(attrs={'class':'form-control'}),
            'telefono': forms.TextInput(attrs={'class':'form-control'}),
            'activo' : forms.Select(choices=Opcion)
        }
#####################################################################        
#class Form_tipo(forms.Form):
#    nombre=forms.CharField()

class Form_tipo(forms.ModelForm):
    class Meta:
        model = Tipo
        fields = [
            'nombre',
            'activo',
        ]
        labels = {
            'nombre':'Nombre',
            'activo' : 'Activo',
        }
        Opcion = ['SS','NN']
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'activo' : forms.Select(choices=Opcion)
        } 
###########################################################   
#class Form_material(forms.Form):
#    codigo=forms.CharField()
#    descripcion=forms.CharField()
#    id_tipo=forms.IntegerField()
class Form_material(forms.ModelForm):
    class Meta:
        model = Material
        fields = [
            'codigo',
            'descripcion',
            'id_tipo',
            'activo',
        ]
        labels = {
            'codigo':'Código',
            'descripcion':'Descripción',
            'id_tipo':'Tipo de material',
            'activo' : 'Activo',
        }
        Opcion = ['SS','NN']
        widgets = {
            'codigo': forms.TextInput(attrs={'class':'form-control'}),
            'descripcion': forms.TextInput(attrs={'class':'form-control'}),
            'id_tipo': forms.Select(attrs={'class':'form-control'}),
            'activo' : forms.Select(choices=Opcion)
        }

####################################################
"""class Form_rents(forms.Form):
    id_cliente=forms.IntegerField()
    id_material=forms.IntegerField()
    fecha_alq=forms.DateField(input_formats=['%d/%m/%Y'])
    hora_alq=forms.DateField(input_formats=['%H:%M'])
    fecha_dev_est=forms.DateField(input_formats=['%d/%m/%Y'])
    hora_dev_est=forms.DateField(input_formats=['%H:%M'])
    #recargo=forms.BooleanField()
    #devuelto=forms.BooleanField()
    pagado=forms.BooleanField()
    importe=forms.FloatField()"""
#---------------------------------------
class  Form_rents(forms.ModelForm):
    class Meta:
        model = Rents
        fields = [
            'id_cliente',
            'id_material',
            'fecha_alq',
            'hora_alq',
            'fecha_dev_est',
            'hora_dev_est',
            'pagado',
            'importe',
        ]
        labels = {
            'id_cliente':'Cliente',
            'id_material':'Material',
            'fecha_alq':'Fecha de alquiler',
            'hora_alq':'Hora de alquiler',
            'fecha_dev_est':'Fecha estimada devol',
            'hora_dev_est':'Hora estimada devol',
            'pagado':'Pagado?',
            'importe':'Importe $',
        }
        Opcion = ['SS','NN']
        widgets = {
            'id_cliente': forms.Select(attrs={'class':'form-control'}),
            'id_material': forms.Select(attrs={'class':'form-control'}),
            'fecha_alq': DateInput(),
            'hora_alq': TimeInput(),
            'fecha_dev_est': DateInput(),
            'hora_dev_est': TimeInput(),
            #'hora_dev_est': widgets.AdminTimeWidget(minute_step=15, second_step=30, twelve_hr=True),
            #'pagado': forms.BooleanField(),
            #'pagado': forms.Checkbox(attrs={'class':'form-control','placeholder':'SI/NO'}),
            #'pagado': CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'pagado': forms.Select(choices=Opcion),
            'importe': forms.TextInput(attrs={'type':'number'}),
        }

class Form_usuarios(forms.ModelForm):
    class Meta:
        model = Usuarios
        fields = [
            'nombre',
            'clave',
            'permiso',
            'activo',
        ]
        labels = {
            'nombre':'Nombre',
            'clave':'Clave',
            'permiso':'Permiso',
            'activo' : 'Activo',
        }
        Opcion = ['SS','NN']
        Opcion2 = [('admin','admin'),('mostrador','mostrador')]
        widgets = {
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'clave': forms.PasswordInput(attrs={'class':'form-control'}),
            'permiso': forms.Select(choices= Opcion2),
            'activo' : forms.Select(choices=Opcion),
        }