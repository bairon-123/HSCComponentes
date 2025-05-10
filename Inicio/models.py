from django import forms
from django.conf import settings
from django.db import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import render



class Cliente(models.Model):
    nombre = models.CharField(max_length=100)

class Tipousuario(models.Model):
    idtipousuario = models.IntegerField(db_column='IDTIPOUSUARIO', primary_key=True)
    nombretipo = models.CharField(db_column='NOMBRETIPO', max_length=30)

    class Meta:
        managed = False
        db_table = 'INICIO_TIPOUSUARIO'

    def __str__(self):
        return self.nombretipo

class Usuario(models.Model):
    username = models.CharField(db_column='USERNAME', primary_key=True, max_length=15)
    contrasennia = models.CharField(db_column='CONTRASENNIA', max_length=30)
    nombre = models.CharField(db_column='NOMBRE', max_length=60)
    apellido = models.CharField(db_column='APELLIDO', max_length=60)
    email = models.CharField(db_column='EMAIL', max_length=150)
    tipousuario = models.ForeignKey('Tipousuario', models.DO_NOTHING, db_column='TIPOUSUARIO_ID')

    class Meta:
        managed = False
        db_table = 'INICIO_USUARIO'

    def __str__(self):
        return self.nombre

class Comuna(models.Model):
    idcomuna = models.IntegerField(db_column='IDCOMUNA', primary_key=True)
    nombrecom = models.CharField(db_column='NOMBRECOM', max_length=40)

    class Meta:
        managed = False
        db_table = 'INICIO_COMUNA'

    def __str__(self):
        return self.nombrecom
    
class Region(models.Model):
    idregion = models.IntegerField(db_column='IDREGION', primary_key=True)
    nombrereg = models.CharField(db_column='NOMBREREG', max_length=40)

    class Meta:
        managed = False
        db_table = 'INICIO_REGION'

    def __str__(self):
        return self.nombrereg

class Direccion(models.Model):
    iddireccion = models.IntegerField(db_column='IDDIRECCION', primary_key=True)
    descripciondir = models.TextField(db_column='DESCRIPCIONDIR')
    region = models.ForeignKey('Region', models.DO_NOTHING, db_column='REGION_ID', null=True)
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='USUARIO_ID')
    comuna = models.ForeignKey('Comuna', models.DO_NOTHING, db_column='COMUNA_ID', null=True)


    class Meta:
        managed = False
        db_table = 'INICIO_DIRECCION'

    def __str__(self):
        return self.descripciondir


class Venta(models.Model):
    idventa = models.IntegerField(db_column='IDVENTA', primary_key=True)
    fechaventa = models.DateField(db_column='FECHAVENTA')
    usuario = models.ForeignKey('Usuario', models.DO_NOTHING, db_column='USUARIO_ID')

    class Meta:
        managed = False
        db_table = 'INICIO_VENTA'

    def __str__(self):
        return str(self.fechaventa)

class Categoria(models.Model):
    idcategoria = models.IntegerField(db_column='IDCATEGORIA', primary_key=True)
    nombrecat = models.CharField(db_column='NOMBRECAT', max_length=30)

    class Meta:
        managed = False
        db_table = 'INICIO_CATEGORIA'

    def __str__(self):
        return self.nombrecat

class Tipoprod(models.Model):
    idtiporod = models.IntegerField(db_column='IDTIPOROD', primary_key=True)
    nombretipoprod = models.CharField(db_column='NOMBRETIPOPROD', max_length=60)

    class Meta:
        managed = False
        db_table = 'INICIO_TIPOPROD'

    def __str__(self):
        return self.nombretipoprod

class Marca(models.Model):
    idmarca = models.IntegerField(db_column='IDMARCA', primary_key=True)
    nombremarca = models.CharField(db_column='NOMBREMARCA', max_length=30)

    class Meta:
        managed = False
        db_table = 'INICIO_MARCA'

    def __str__(self):
        return self.nombremarca

class Modelo(models.Model):
    idmodelo = models.IntegerField(db_column='IDMODELO', primary_key=True)
    nombremodelo = models.CharField(db_column='NOMBREMODELO', max_length=30)
    marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='MARCA_ID')

    class Meta:
        managed = False
        db_table = 'INICIO_MODELO'

    def __str__(self):
        return self.nombremodelo

class Producto(models.Model):
    idproducto = models.IntegerField(db_column='IDPRODUCTO', primary_key=True)
    nombreproducto = models.CharField(db_column='NOMBREPRODUCTO', max_length=50)
    precioproducto = models.IntegerField(db_column='PRECIOPRODUCTO')
    especificacionprod = models.CharField(db_column='ESPECIFICACIONPROD', max_length=900)
    stockprod = models.IntegerField(db_column='STOCKPROD')
    imagenprod = models.CharField(db_column='IMAGENPROD', max_length=100)
    marca = models.ForeignKey('Marca', models.DO_NOTHING, db_column='MARCA_ID')
    tipoprod = models.ForeignKey('Tipoprod', models.DO_NOTHING, db_column='TIPOPROD_ID')

    class Meta:
        managed = False
        db_table = 'INICIO_PRODUCTO'

    def __str__(self):
        return self.nombreproducto

class Detalle(models.Model):
    iddetalle = models.IntegerField(db_column='IDDETALLE', primary_key=True)
    cantidad = models.IntegerField(db_column='CANTIDAD')
    subtotal = models.IntegerField(db_column='SUBTOTAL')
    venta = models.ForeignKey('Venta', models.DO_NOTHING, db_column='VENTA_ID')
    producto = models.ForeignKey('Producto', models.DO_NOTHING, db_column='PRODUCTO_ID')

    class Meta:
        managed = False
        db_table = 'INICIO_DETALLE'

    def __str__(self):
        return str(self.subtotal)

  

class Carrito(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = 'carrito'
    
class Compra(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.usuario} el {self.fecha.strftime('%Y-%m-%d')}"
        
class DetalleCompra(models.Model):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombreproducto} (Compra {self.compra.id})"
    

