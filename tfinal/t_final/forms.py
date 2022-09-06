from django import forms

class Form_clientes(forms.Form):
    nombre=forms.CharField()
    dni=forms.CharField()
    fecha_nacimiento=forms.DateField()
    domicilio=forms.CharField()
    telefono=forms.CharField()

class Form_tipo(forms.Form):
    nombre=forms.CharField()
    
class Form_material(forms.Form):
    codigo=forms.CharField()
    descripcion=forms.CharField()
    tipo_material=forms.IntegerField()

class Form_rents(forms.Form):
    cliente=forms.IntegerField()
    material=forms.IntegerField()
    fecha_alquiler=forms.DateField()
    hora_alquiler=forms.DateField()
    fecha_estimada_devolucion=forms.DateField()
    hora_estimada_devolucion=forms.DateField()
    recargo=forms.BooleanField()
    devuelto=forms.BooleanField()
    pagado=forms.BooleanField()
    importe=forms.FloatField()
