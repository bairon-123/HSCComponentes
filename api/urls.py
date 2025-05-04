from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'productos', views.ProductoViewSet)
router.register(r'marcas', views.MarcaViewSet)
router.register(r'tipos-producto', views.TipoProdViewSet)
router.register(r'carrito', views.CarritoViewSet, basename='carrito')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]