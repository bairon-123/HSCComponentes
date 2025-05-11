from django.db import models
from APIs.sales.models import Venta

class TransaccionPago(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    referencia = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(max_length=20)  # 'pendiente', 'completado', 'fallido'
    metodo = models.CharField(max_length=50)  # 'tarjeta', 'transferencia', etc.

