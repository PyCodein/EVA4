from django.contrib import admin
from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Configuración del esquema de Swagger
schema_view = get_schema_view(
    openapi.Info(
        title="API de Tareas",
        default_version='v1',
        description="Documentación de la API para la gestión de tareas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@tareas.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # Otras URLs de tu proyecto aquí, por ejemplo:
    # path('api/tasks/', include('myapp.urls')),
    
    # URLs de Swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger-json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
