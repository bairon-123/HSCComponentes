from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'envios', views.EnvioViewSet, basename='envio')

urlpatterns = [
    path('', include(router.urls)),
    # Puedes agregar endpoints adicionales aquí si lo necesitas
]