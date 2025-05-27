from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from typing import List, Optional

from ..models.task import Task, Subtask
from ..schemas.task import TaskCreate, TaskUpdate, SubtaskCreate

def create_task(db: Session, task: TaskCreate, user_id: int) -> Task:
    """Crea una nueva tarea para el usuario."""
    db_task = Task(**task.model_dump(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_user_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100) -> List[Task]:
    """Obtiene todas las tareas de un usuario."""
    return db.query(Task).filter(Task.user_id == user_id).offset(skip).limit(limit).all()

def get_user_tasks_by_status(
    db: Session, 
    user_id: int, 
    completed: bool,
    skip: int = 0, 
    limit: int = 100
) -> List[Task]:
    """
    Obtiene las tareas de un usuario filtradas por estado de completado.
    
    Args:
        db: Sesión de la base de datos
        user_id: ID del usuario
        completed: True para tareas completadas, False para tareas pendientes
        skip: Número de registros a saltar (para paginación)
        limit: Número máximo de registros a devolver
    
    Returns:
        Lista de tareas que coinciden con los criterios
    """
    return (
        db.query(Task)
        .filter(Task.user_id == user_id, Task.completed == completed)
        .order_by(Task.created_at.desc())  # Ordenadas por fecha de creación, más recientes primero
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_task(db: Session, task_id: int, user_id: int) -> Task:
    """Obtiene una tarea específica del usuario."""
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarea no encontrada"
        )
    return task

def update_task(db: Session, task_id: int, user_id: int, task_update: TaskUpdate) -> Task:
    """Actualiza una tarea existente."""
    task = get_task(db, task_id, user_id)
    
    update_data = task_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(task, field, value)
        
        # Si la tarea se marca como completada, completar todas las subtareas
        if field == 'completed' and value is True:
            for subtask in task.subtasks:
                subtask.completed = True
    
    db.commit()
    db.refresh(task)
    return task

def delete_task(db: Session, task_id: int, user_id: int) -> None:
    """Elimina una tarea y todas sus subtareas."""
    task = get_task(db, task_id, user_id)
    
    # Las subtareas se eliminarán automáticamente debido a la relación cascade
    # definida en el modelo Task: cascade="all, delete-orphan"
    db.delete(task)
    db.commit()

def validate_task_ownership(db: Session, task_id: int, user_id: int) -> Task:
    """Valida que una tarea exista y pertenezca al usuario."""
    task = db.query(Task).filter(Task.id == task_id, Task.user_id == user_id).first()
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Tarea principal no encontrada o no tienes permiso para acceder a ella"
        )
    return task

def get_subtask(db: Session, subtask_id: int, task_id: int) -> Subtask:
    """Obtiene una subtarea específica."""
    subtask = db.query(Subtask).filter(Subtask.id == subtask_id, Subtask.task_id == task_id).first()
    if not subtask:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Subtarea no encontrada"
        )
    return subtask

def create_subtask(db: Session, task_id: int, user_id: int, subtask: SubtaskCreate) -> Subtask:
    """Crea una nueva subtarea."""
    # Verificar que la tarea principal existe y pertenece al usuario
    task = validate_task_ownership(db, task_id, user_id)
    
    db_subtask = Subtask(**subtask.model_dump(), task_id=task_id)
    db.add(db_subtask)
    db.commit()
    db.refresh(db_subtask)
    return db_subtask

def update_subtask(db: Session, subtask_id: int, task_id: int, user_id: int, completed: bool) -> Subtask:
    """Actualiza el estado de una subtarea."""
    # Verificar que la tarea principal existe y pertenece al usuario
    task = validate_task_ownership(db, task_id, user_id)
    
    # Obtener y validar la subtarea
    subtask = get_subtask(db, subtask_id, task_id)
    
    subtask.completed = completed
    db.commit()
    db.refresh(subtask)
    return subtask

def delete_subtask(db: Session, subtask_id: int, task_id: int, user_id: int) -> None:
    """Elimina una subtarea."""
    # Verificar que la tarea principal existe y pertenece al usuario
    task = validate_task_ownership(db, task_id, user_id)
    
    # Obtener y validar la subtarea
    subtask = get_subtask(db, subtask_id, task_id)
    
    db.delete(subtask)
    db.commit() 