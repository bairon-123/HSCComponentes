from rest_framework import viewsets
from .models import Categoria, Almacen, ItemInventario
from .serializers import CategoriaSerializer, AlmacenSerializer, ItemInventarioSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from django.shortcuts import render

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class AlmacenViewSet(viewsets.ModelViewSet):
    queryset = Almacen.objects.all()
    serializer_class = AlmacenSerializer

class ItemInventarioViewSet(viewsets.ModelViewSet):
    queryset = ItemInventario.objects.all().select_related('producto', 'almacen')
    serializer_class = ItemInventarioSerializer
    
    # Endpoint adicional para obtener el stock total de un producto en todos los almacenes
    @action(detail=False, methods=['get'], url_path='stock-total/(?P<producto_id>[^/.]+)')
    def stock_total(self, request, producto_id=None):
        total = ItemInventario.objects.filter(
            producto_id=producto_id
        ).aggregate(
            total_stock=Sum('cantidad')
        )['total_stock'] or 0
        
        return Response({'producto_id': producto_id, 'stock_total': total})
    
    # Endpoint para obtener items por almacén
    @action(detail=False, methods=['get'], url_path='por-almacen/(?P<almacen_id>[^/.]+)')
    def por_almacen(self, request, almacen_id=None):
        items = ItemInventario.objects.filter(almacen_id=almacen_id)
        serializer = self.get_serializer(items, many=True)
        return Response(serializer.data) 

