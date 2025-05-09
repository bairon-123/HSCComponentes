from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

class ProcesarPagoView(APIView):
    def post(self, request):
        # Datos del pago desde el request
        data = request.data
        
        # Integración con API externa de pagos (ejemplo)
        try:
            response = requests.post(
                'https://api.pagos-externos.com/v1/transactions',
                json=data,
                headers={'Authorization': 'Bearer TU_API_KEY'}
            )
            
            if response.status_code == 201:
                # Guardar transacción en la base de datos
                # ...
                return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
            else:
                return Response(response.json(), status=response.status_code)
                
        except requests.exceptions.RequestException as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
def test_pago(request):
    return Response({"mensaje": "✅ Endpoint de prueba en pagos funcionando correctamente"})