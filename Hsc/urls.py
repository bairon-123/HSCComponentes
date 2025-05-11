"""Hsc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView 

urlpatterns = [
    path('admin/', admin.site.urls),  # Panel admin Django
    path('', include('Inicio.urls')),
    path('api/', include('api.urls')),  # Rutas API REST
    path('schema/', get_schema_view(  # OpenAPI JSON schema
        title="HSC Componentes",
        description="API para el sistema de HSC Componentes",
        version="1.0.0"
    ), name='openapi-schema'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema')),
    path('api/inventario/', include('APIs.inventory.urls')),
    path('api/pagos/', include('APIs.payments.urls')),
    path('api/ventas/', include('APIs.sales.urls')),
    path('api/envios/', include('APIs.shipping.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


