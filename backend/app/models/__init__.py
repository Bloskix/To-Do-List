"""
Inicialización del paquete models
""" 

from app.database import Base
from .user import User
from .task import Task, Subtask

# Esto asegura que todas las tablas compartan la misma Base
__all__ = ['Base', 'User', 'Task', 'Subtask'] 