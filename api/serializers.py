from rest_framework import serializers
from Inicio.models import Producto, Marca, TipoProd, Carrito, Usuario

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ['id', 'nombremarca']

class TipoProdSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProd
        fields = ['id', 'nombretipoprod']

class ProductoSerializer(serializers.ModelSerializer):
    marca = MarcaSerializer()
    TipoProd = TipoProdSerializer()
    imagen_url = serializers.SerializerMethodField()

    class Meta:
        model = Producto
        fields = ['idproducto', 'nombreproducto', 'precioproducto', 
                'especificacionprod', 'stockprod', 'imagen_url', 
                'marca', 'tipoprod']

    def get_imagen_url(self, obj):
        if obj.imagenprod:
            return self.context['request'].build_absolute_uri(obj.imagenprod.url)
        return None

class CarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrito
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'nombre', 'apellido', 'email']