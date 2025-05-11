from django.contrib import admin
from .models import Tipousuario, Usuario, Venta, Categoria, Tipoprod, Marca, Modelo, Producto, Region, Comuna, Direccion, Detalle

# Registro de todos los modelos (incluye Modelo solo una vez)
modelos = [Tipousuario, Usuario, Venta, Categoria, Tipoprod, Marca, Modelo, Producto, Region, Comuna, Direccion, Detalle]

for modelo in modelos:
    admin.site.register(modelo)