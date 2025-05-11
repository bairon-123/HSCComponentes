from django.db import models
from APIs.sales.models import Venta

class Envio(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('EN_PROCESO', 'En proceso'),
        ('EN_TRANSITO', 'En tránsito'),
        ('ENTREGADO', 'Entregado'),
        ('CANCELADO', 'Cancelado'),
    ]

    venta = models.OneToOneField(Venta, on_delete=models.CASCADE, related_name='envio')
    codigo_seguimiento = models.CharField(max_length=50, unique=True)
    direccion_envio = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    transportista = models.CharField(max_length=100)
    costo_envio = models.DecimalField(max_digits=10, decimal_places=2)
    url_seguimiento = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"Envío {self.codigo_seguimiento} - {self.get_estado_display()}"
