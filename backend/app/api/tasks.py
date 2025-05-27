from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from ..core.security import get_current_user
from ..schemas.task import Task, TaskCreate, TaskUpdate, Subtask, SubtaskCreate
from ..services.task_service import (
    create_task, get_user_tasks, get_task, update_task, delete_task,
    create_subtask, update_subtask, delete_subtask, get_user_tasks_by_status
)
from ..database import get_db
from ..models.user import User

router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
    responses={401: {"description": "No autorizado"}}
)

@router.post("", response_model=Task, status_code=status.HTTP_201_CREATED,
            summary="Crear tarea",
            description="Crea una nueva tarea para el usuario autenticado.")
def create_task_endpoint(
    task: TaskCreate,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Crea una nueva tarea con:
    - **title**: Título de la tarea
    - **start_date**: Fecha de inicio (opcional)
    - **end_date**: Fecha de finalización (opcional)
    - **completed**: Estado de completado (por defecto False)
    """
    # Obtener el ID del usuario
    user = db.query(User).filter(User.email == current_user_email).first()
    return create_task(db, task, user.id)

@router.get("", response_model=List[Task],
           summary="Listar tareas",
           description="Obtiene todas las tareas del usuario autenticado.")
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Obtiene la lista de tareas del usuario con paginación:
    - **skip**: Número de tareas a saltar
    - **limit**: Número máximo de tareas a devolver
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    return get_user_tasks(db, user.id, skip, limit)

@router.get("/{task_id}", response_model=Task,
           summary="Obtener tarea",
           description="Obtiene una tarea específica del usuario autenticado.")
def read_task(
    task_id: int,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Obtiene una tarea específica por su ID:
    - **task_id**: ID de la tarea a obtener
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    return get_task(db, task_id, user.id)

@router.put("/{task_id}", response_model=Task,
           summary="Actualizar tarea",
           description="Actualiza una tarea existente del usuario autenticado.")
def update_task_endpoint(
    task_id: int,
    task_update: TaskUpdate,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Actualiza una tarea existente:
    - **task_id**: ID de la tarea a actualizar
    - **title**: Nuevo título (opcional)
    - **start_date**: Nueva fecha de inicio (opcional)
    - **end_date**: Nueva fecha de finalización (opcional)
    - **completed**: Nuevo estado de completado (opcional)
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    return update_task(db, task_id, user.id, task_update)

@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT,
              summary="Eliminar tarea",
              description="Elimina una tarea existente del usuario autenticado.")
def delete_task_endpoint(
    task_id: int,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Elimina una tarea por su ID:
    - **task_id**: ID de la tarea a eliminar
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    delete_task(db, task_id, user.id)

# Endpoints para subtareas
@router.post("/{task_id}/subtasks", response_model=Subtask,
            summary="Crear subtarea",
            description="Crea una nueva subtarea para una tarea existente.")
def create_subtask_endpoint(
    task_id: int,
    subtask: SubtaskCreate,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Crea una nueva subtarea:
    - **task_id**: ID de la tarea padre
    - **title**: Título de la subtarea
    - **completed**: Estado de completado (por defecto False)
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    return create_subtask(db, task_id, user.id, subtask)

@router.put("/{task_id}/subtasks/{subtask_id}", response_model=Subtask,
           summary="Actualizar subtarea",
           description="Actualiza el estado de una subtarea existente.")
def update_subtask_endpoint(
    task_id: int,
    subtask_id: int,
    completed: bool,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Actualiza el estado de una subtarea:
    - **task_id**: ID de la tarea padre
    - **subtask_id**: ID de la subtarea
    - **completed**: Nuevo estado de completado
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    return update_subtask(db, subtask_id, task_id, user.id, completed)

@router.delete("/{task_id}/subtasks/{subtask_id}", status_code=status.HTTP_204_NO_CONTENT,
              summary="Eliminar subtarea",
              description="Elimina una subtarea existente.")
def delete_subtask_endpoint(
    task_id: int,
    subtask_id: int,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Elimina una subtarea:
    - **task_id**: ID de la tarea padre
    - **subtask_id**: ID de la subtarea a eliminar
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    delete_subtask(db, subtask_id, task_id, user.id)

@router.get("/status/{completed}", response_model=List[Task],
           summary="Listar tareas por estado",
           description="Obtiene las tareas del usuario filtradas por estado de completado.")
def read_tasks_by_status(
    completed: bool,
    skip: int = 0,
    limit: int = 100,
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """
    Obtiene la lista de tareas del usuario filtradas por estado:
    - **completed**: True para tareas completadas, False para pendientes
    - **skip**: Número de tareas a saltar (para paginación)
    - **limit**: Número máximo de tareas a devolver
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    return get_user_tasks_by_status(db, user.id, completed, skip, limit) 