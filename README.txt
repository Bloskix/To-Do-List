# 📝 To-Do List App

Una aplicación moderna de lista de tareas que permite gestionar tus actividades diarias, con soporte para modo sin conexión.

## ✨ Características

- 📱 **Modo Sin Conexión**: Trabaja sin necesidad de iniciar sesión, con almacenamiento local
- ✅ **Gestión de Tareas**: Crea, edita y marca como completadas tus tareas
- 📋 **Subtareas**: Divide tus tareas en pasos más pequeños
- 📅 **Fechas**: Establece fechas de inicio y fin para tus tareas
- 🔒 **Sincronización**: Guarda tus tareas en la nube al iniciar sesión
- 🎨 **Interfaz Moderna**: Diseño limpio y responsive con Tailwind CSS

## 🛠️ Tecnologías

### Frontend
- **Next.js**: Framework React para desarrollo web full-stack
- **TypeScript**: JavaScript con tipos para mejor calidad de código
- **Zustand**: Gestión de estado simple y efectiva
- **Tailwind CSS**: Framework CSS utilitario
- **Shadcn UI**: Componentes UI reutilizables y accesibles

### Backend
- **Python**: Lenguaje principal del backend
- **FastAPI**: Framework web moderno y rápido
- **PostgreSQL**: Base de datos relacional
- **JWT & OAuth**: Autenticación y autorización

## 🚀 Inicio Rápido

### Prerrequisitos
- Node.js
- pnpm
- Python 3.x
- PostgreSQL

### Configuración del Frontend

1. Instalar dependencias:
```bash
# Navegar al directorio frontend
cd frontend

# Instalar dependencias base
pnpm add zustand @tanstack/react-query zod react-hook-form @hookform/resolvers

# Instalar dependencias de UI
pnpm add @radix-ui/react-dialog @radix-ui/react-slot lucide-react clsx tailwind-merge class-variance-authority uuid

# Instalar dependencias de desarrollo
pnpm add -D @types/uuid @shadcn/ui

# Configurar Shadcn UI
pnpm dlx shadcn-ui@latest init
```

2. Crear archivo `.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

3. Iniciar el servidor de desarrollo:
```bash
pnpm dev
```

### Configuración del Backend

1. Crear entorno virtual:
```bash
# Navegar al directorio backend
cd backend

# Crear y activar entorno virtual
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar variables de entorno:
Crear archivo `.env` en el directorio backend:
```env
DB_HOST=localhost
DB_PORT=5432
DB_NAME=todo_db
DB_USER=your_user
DB_PASSWORD=your_password
```

4. Ejecutar migraciones:
```bash
alembic upgrade head
```

5. Iniciar servidor:
```bash
uvicorn main:app --reload
```

## 🌟 Características Especiales

### Modo Sin Conexión
- Trabaja sin necesidad de crear una cuenta
- Almacenamiento local de tareas
- Opción de sincronizar más tarde

### Sincronización
- Al iniciar sesión, tus tareas se sincronizan automáticamente
- Accede a tus tareas desde cualquier dispositivo
- No pierdes tus tareas locales al sincronizar

## 🤝 Contribución

1. Fork el proyecto
2. Crea tu rama de características (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add: alguna característica'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📄 Licencia

Distribuido bajo la Licencia MIT. Ver `LICENSE` para más información.