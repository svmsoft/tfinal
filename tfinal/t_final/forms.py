from django import forms



class Form_clientes(forms.Form):
    nombre=forms.CharField()
    dni=forms.CharField()
    fecha_nac=forms.DateField(input_formats=['%d/%m/%Y'])
    domicilio=forms.CharField()
    telefono=forms.CharField()

class Form_tipo(forms.Form):
    nombre=forms.CharField()
    
class Form_material(forms.Form):
    codigo=forms.CharField()
    descripcion=forms.CharField()
    id_tipo=forms.IntegerField()

class Form_rents(forms.Form):
    id_cliente=forms.IntegerField()
    id_material=forms.IntegerField()
    fecha_alq=forms.DateField(input_formats=['%d/%m/%Y'])
    hora_alq=forms.DateField(input_formats=['%H:%M'])
    fecha_dev_est=forms.DateField(input_formats=['%d/%m/%Y'])
    hora_dev_est=forms.DateField(input_formats=['%H:%M'])
    #recargo=forms.BooleanField()
    #devuelto=forms.BooleanField()
    pagado=forms.BooleanField()
    importe=forms.FloatField()
