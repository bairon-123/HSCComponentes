from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from Inicio.models import Producto, Marca, Tipoprod, Carrito
from .serializers import (ProductoSerializer, MarcaSerializer, TipoProdSerializer, CarritoSerializer)
from django.shortcuts import get_object_or_404

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    @action(detail=False, methods=['get'])
    def por_categoria(self, request):
        tipo = request.query_params.get('tipo')
        if tipo:
            productos = Producto.objects.filter(TipoProd__nombreTipoProd__iexact=tipo)
            serializer = self.get_serializer(productos, many=True)
            return Response(serializer.data)
        return Response([])

class MarcaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Marca.objects.all()
    serializer_class = MarcaSerializer

class TipoProdViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tipoprod.objects.all()
    serializer_class = TipoProdSerializer

class CarritoViewSet(viewsets.ModelViewSet):
    serializer_class = CarritoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Carrito.objects.filter(usuario=self.request.user)

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)

    @action(detail=True, methods=['post'])
    def actualizar_cantidad(self, request, pk=None):
        carrito = get_object_or_404(Carrito, pk=pk, usuario=request.user)
        cantidad = request.data.get('cantidad')
        
        if cantidad and cantidad.isdigit():
            carrito.cantidad = int(cantidad)
            carrito.save()
            return Response({'status': 'cantidad actualizada'})
        return Response({'error': 'cantidad inválida'}, 
                    status=status.HTTP_400_BAD_REQUEST)

