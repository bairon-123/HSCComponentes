from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'almacenes', views.AlmacenViewSet)
router.register(r'items-inventario', views.ItemInventarioViewSet, basename='iteminventario')

urlpatterns = [
    path('', include(router.urls)),
    
    # podemos agregar URLs adicionales fuera del router:
    # path('reporte-inventario/', views.ReporteInventarioView.as_view(), name='reporte-inventario'),
]