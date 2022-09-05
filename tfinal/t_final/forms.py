from django import forms

class From_clientes(forms.form):
    nombre=forms.CharField()
    dni=forms.CharField()
    fecha_nacimiento=forms.DateField()
    domicilio=forms.CharField()
    telefono=forms.CharField()

class From_tipo(forms.form):
    nombre=forms.CharField()
    
class From_material(forms.form):
    codigo=forms.CharField()
    descripcion=forms.CharField()
    tipo_material=forms.IntegerField()

class From_rents(forms.form):
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
