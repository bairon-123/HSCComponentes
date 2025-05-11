from django.urls import path
from . import views
from django.urls import path
from .views import ProcesarPagoView


urlpatterns = [
    path('test/', views.test_pago, name='test_pago'),
    path('procesar/', ProcesarPagoView.as_view(), name='procesar_pago'),
]



