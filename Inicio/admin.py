from django.contrib import admin
from .models import Tipousuario, Usuario, Venta, Categoria, Tipoprod, Marca, Modelo, Producto, Region, Comuna, Direccion, Detalle

# Registro básico
admin.site.register(Tipousuario)
admin.site.register(Usuario)
admin.site.register(Venta)
admin.site.register(Categoria)
admin.site.register(Tipoprod)
admin.site.register(Marca)
admin.site.register(Modelo)
admin.site.register(Producto)
admin.site.register(Region)
admin.site.register(Comuna)
admin.site.register(Direccion)
admin.site.register(Detalle)

