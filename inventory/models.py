from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

class Almacen(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.TextField()

class ItemInventario(models.Model):
    producto = models.ForeignKey('sales.Producto', on_delete=models.CASCADE)
    almacen = models.ForeignKey(Almacen, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha_actualizacion = models.DateTimeField(auto_now=True)

