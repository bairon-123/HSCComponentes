from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Envio
from .serializers import EnvioSerializer, CrearEnvioSerializer
import requests
from django.conf import settings

class EnvioViewSet(viewsets.ModelViewSet):
    queryset = Envio.objects.all().select_related('venta')
    serializer_class = EnvioSerializer

    @action(detail=False, methods=['post'], url_path='crear-externo')
    def crear_envio_externo(self, request):
        serializer = CrearEnvioSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # Datos para la API externa
        data = {
            'venta_id': serializer.validated_data['venta_id'],
            'direccion': serializer.validated_data['direccion_envio'],
            'transportista': serializer.validated_data['transportista'],
            'costo': float(serializer.validated_data['costo_envio'])
        }

        try:
            # Configuración para la API externa (ejemplo)
            headers = {
                'Authorization': f'Bearer {settings.SHIPPING_API_KEY}',
                'Content-Type': 'application/json'
            }

            response = requests.post(
                'https://api.envios-externos.com/v1/shipments',
                json=data,
                headers=headers,
                timeout=10
            )

            if response.status_code == 201:
                # Guardar en nuestra base de datos
                envio_data = response.json()
                envio = Envio.objects.create(
                    venta_id=serializer.validated_data['venta_id'],
                    codigo_seguimiento=envio_data['tracking_code'],
                    direccion_envio=serializer.validated_data['direccion_envio'],
                    estado='PENDIENTE',
                    transportista=serializer.validated_data['transportista'],
                    costo_envio=serializer.validated_data['costo_envio'],
                    url_seguimiento=envio_data.get('tracking_url', '')
                )
                return Response(EnvioSerializer(envio).data, status=status.HTTP_201_CREATED)
            
            return Response(response.json(), status=response.status_code)

        except requests.exceptions.RequestException as e:
            return Response(
                {'error': 'Error al conectar con el servicio de envíos', 'details': str(e)},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

    @action(detail=True, methods=['get'], url_path='actualizar-estado')
    def actualizar_estado(self, request, pk=None):
        envio = self.get_object()
        
        try:
            # Consultar API externa para estado actual
            headers = {
                'Authorization': f'Bearer {settings.SHIPPING_API_KEY}'
            }
            
            response = requests.get(
                f'https://api.envios-externos.com/v1/shipments/{envio.codigo_seguimiento}',
                headers=headers,
                timeout=5
            )
            
            if response.status_code == 200:
                data = response.json()
                envio.estado = data['status']
                envio.url_seguimiento = data.get('tracking_url', envio.url_seguimiento)
                envio.save()
                return Response(EnvioSerializer(envio).data)
            
            return Response(response.json(), status=response.status_code)
            
        except requests.exceptions.RequestException as e:
            return Response(
                {'error': 'Error al conectar con el servicio de envíos', 'details': str(e)},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )