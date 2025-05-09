from rest_framework import serializers
from .models import Categoria, Almacen, ItemInventario
from sales.serializers import ProductoSerializer  # Importamos el serializer de Producto si necesitamos anidar datos

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class AlmacenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Almacen
        fields = '__all__'

class ItemInventarioSerializer(serializers.ModelSerializer):
    # Opcional: Anidar información del producto en lugar de solo mostrar el ID
    producto = ProductoSerializer(read_only=True)
    
    # Opcional: Anidar información del almacén
    almacen = AlmacenSerializer(read_only=True)
    
    class Meta:
        model = ItemInventario
        fields = '__all__'
        # Si prefieres controlar qué campos mostrar explícitamente:
        # fields = ['id', 'producto', 'almacen', 'cantidad', 'fecha_actualizacion']