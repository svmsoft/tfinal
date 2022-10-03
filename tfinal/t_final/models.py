from importlib.util import module_for_loader
from django.db import models

# Create your models here

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    activo = models.CharField(max_length=5, null=True)
    def __str__(self):
        return '{}'.format(self.nombre)

    
class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    fecha_nac = models.DateField()
    domicilio = models.CharField(max_length=100)
    telefono = models.CharField(max_length=50)
    activo = models.CharField(max_length=5, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Usuarios(models.Model):
    nombre = models.CharField(max_length=50)
    clave = models.CharField(max_length=50)
    permiso = models.CharField(max_length=50, null=True)
    activo = models.CharField(max_length=5, null=True)

    def __str__(self):
        return '{}'.format(self.nombre)

class Material(models.Model):
    codigo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    id_tipo = models.ForeignKey(Tipo, null=True, blank=True, on_delete=models.CASCADE)
    activo = models.CharField(max_length=5, null=True)   
    #id_tipo = models.IntegerField()
    def __str__(self):
        return '{}'.format(self.codigo)
    
class Rents(models.Model):
    id_cliente = models.ForeignKey(Clientes, null=True, blank=True, on_delete=models.CASCADE)
    #id_cliente = models.IntegerField()
    id_material = models.ForeignKey(Material, null=True, blank=True, on_delete=models.CASCADE)
    #id_material = models.IntegerField()
    fecha_alq = models.DateField()
    hora_alq = models.CharField(max_length=20)
    fecha_dev_est = models.DateField()
    hora_dev_est = models.CharField(max_length=20)
    recargo = models.CharField(null=True, max_length=20)
    devuelto = models.CharField(null=True, max_length=20)
    pagado = models.CharField(null=True, max_length=20)
    importe = models.FloatField(null=True, default=0)
    
   # def __str__(self):
       # return f"Cliente: {self.id_cliente}, Material: {self.id_material}, Fecha-alq: {fecha_alq}"

    
    
    
