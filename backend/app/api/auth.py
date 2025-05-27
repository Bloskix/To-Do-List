from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Any

from ..core.security import get_current_user
from ..schemas.user import UserCreate, UserLogin, Token, User as UserSchema
from ..models.user import User
from ..services.user_service import create_user, authenticate_user
from ..database import get_db

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"description": "No autorizado"}}
)

@router.post("/register", response_model=UserSchema, status_code=status.HTTP_201_CREATED,
            summary="Registrar un nuevo usuario",
            description="Crea una nueva cuenta de usuario con email y contraseña.")
def register(user: UserCreate, db: Session = Depends(get_db)) -> Any:
    """
    Registra un nuevo usuario con:
    - **email**: Email único del usuario
    - **username**: Nombre de usuario único
    - **password**: Contraseña del usuario
    """
    return create_user(db, user)

@router.post("/login", response_model=Token,
            summary="Iniciar sesión",
            description="Obtiene un token de acceso usando email y contraseña.")
def login(user_data: UserLogin, db: Session = Depends(get_db)) -> Any:
    """
    Obtiene un token de acceso para:
    - **email**: Email del usuario
    - **password**: Contraseña del usuario
    
    El token devuelto debe ser usado en el header Authorization como:
    `Bearer <token>`
    """
    return authenticate_user(db, user_data)

@router.get("/me", response_model=UserSchema,
            summary="Obtener usuario actual",
            description="Obtiene la información del usuario autenticado usando el token JWT.")
def read_users_me(
    current_user_email: str = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> Any:
    """
    Obtiene la información del usuario autenticado.
    
    Requiere el token JWT en el header de autorización:
    `Authorization: Bearer <token>`
    """
    user = db.query(User).filter(User.email == current_user_email).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Usuario no encontrado"
        )
    return user 