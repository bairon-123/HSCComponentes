from rest_framework import serializers
from .models import Envio
from sales.serializers import VentaSerializer

class EnvioSerializer(serializers.ModelSerializer):
    venta = VentaSerializer(read_only=True)
    
    class Meta:
        model = Envio
        fields = '__all__'
        read_only_fields = ('fecha_creacion', 'fecha_actualizacion')

class CrearEnvioSerializer(serializers.Serializer):
    venta_id = serializers.IntegerField()
    direccion_envio = serializers.CharField()
    transportista = serializers.CharField()
    costo_envio = serializers.DecimalField(max_digits=10, decimal_places=2)

    def validate_venta_id(self, value):
        from sales.models import Venta
        if not Venta.objects.filter(id=value).exists():
            raise serializers.ValidationError("La venta especificada no existe")
        return value