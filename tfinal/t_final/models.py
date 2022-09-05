from importlib.util import module_for_loader
from django.db import models

# Create your models here
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    
class Rents(models.Model):
    id_cliente = models.IntegerField()
    id_material = models.IntegerField()
    fecha_alqu = models.DateField()
    hora_alq = models.DateField()
    fecha_dev_est = models.DateField()
    hora_dev_est = models.DateField()
    recargo = models.BooleanField()
    devuelto = models.BooleanField()
    pagado = models.BooleanField()
    importe = models.FloatField(default=0)
    

class Material(models.Model):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    id_tipo = models.IntegerField()
    
class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    
    
    
