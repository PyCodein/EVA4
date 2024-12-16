from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=100)  # Título de la tarea
    description = models.TextField()           # Descripción de la tarea
    completed = models.BooleanField(default=False)  # Estado de la tarea
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación
    updated_at = models.DateTimeField(auto_now=True)      # Última actualización

    def __str__(self):
        return self.title
