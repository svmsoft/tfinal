from django.db import models

# Create your models here
class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.CharField()
    fecha_nac = models.DateField()
    domicilio = models.CharField()
    telefono = models.CharField()
    
class rents(models.Model):
    id_cliente = models.IntegerField()
    id_material = models.IntegerField()
    fecha_alqu = models.DateField()
    hora_alq = models.DateField()
    fecha_dev_est = models.DateField()
    hora_dev_est = models.DateField()
    recargo = models.BooleanField()
    devuelto = models.BooleanField()
    pagado = models.BooleanField()

class material(models.Model):
    codigo = models.CharField()
    descripcion = models.CharField()
    id_tipo = models.IntegerField()
    
class tipo(models.Model):
    nombre = models.CharField()
    
    
    
