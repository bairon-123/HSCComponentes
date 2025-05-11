from django.contrib import admin
from .models import Envio

@admin.register(Envio)
class EnvioAdmin(admin.ModelAdmin):
    list_display = ('codigo_seguimiento', 'venta', 'estado', 'transportista', 'costo_envio')
    list_filter = ('estado', 'transportista')
    search_fields = ('codigo_seguimiento', 'venta__id')
    readonly_fields = ('fecha_creacion', 'fecha_actualizacion')
