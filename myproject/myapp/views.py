from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer

class TaskListCreate(generics.ListCreateAPIView):
    """
    Vista para listar todas las tareas y crear una nueva tarea.
    Solo accesible para usuarios autenticados.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Asegura que solo usuarios autenticados puedan acceder

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Vista para recuperar, actualizar y eliminar una tarea específica.
    Solo accesible para usuarios autenticados.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Asegura que solo usuarios autenticados puedan acceder
