from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from app.api import auth, tasks
from app.core.config import get_settings

settings = get_settings()

# Configuración de la documentación de la API
description = """
To-Do List API permite gestionar tareas y subtareas.

## Autenticación

* **Registro**: Crea una nueva cuenta de usuario
* **Login**: Obtiene un token de acceso
* **Me**: Obtiene la información del usuario actual (requiere autenticación)
"""

app = FastAPI(
    title="To-Do List API",
    description=description,
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(auth.router)
app.include_router(tasks.router)

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de To-Do List"} 