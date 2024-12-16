from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import TaskListCreate, TaskDetail  # Importa tus vistas

urlpatterns = [
    # Rutas para autenticación JWT
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Para obtener el token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # Para refrescar el token
    
    # Rutas para las tareas
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),  # Listar y crear tareas
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),  # Detalles, actualizar y eliminar tareas
]
