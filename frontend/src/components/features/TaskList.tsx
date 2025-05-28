"use client"

import { useState } from "react"
import { useTaskStore } from "@/store/useTaskStore"
import { LoginDialog } from "./LoginDialog"
import { Button } from "@/components/ui/button"
import { PlusIcon } from "lucide-react"
import { Task } from "@/types/task"

export function TaskList() {
  const [isLoginDialogOpen, setIsLoginDialogOpen] = useState(false)
  const { tasks, isOfflineMode, addTask } = useTaskStore()

  const handleCreateTask = () => {
    if (!isOfflineMode) {
      setIsLoginDialogOpen(true)
      return
    }
    
    // Aquí iría la lógica para crear una nueva tarea
    addTask({
      title: "Nueva tarea",
      startDate: new Date(),
    })
  }

  const handleLogin = () => {
    // Aquí iría la lógica de inicio de sesión
    console.log("Iniciando sesión...")
  }

  return (
    <div className="container mx-auto p-4">
      <div className="flex justify-between items-center mb-6">
        <h1 className="text-2xl font-bold">Mis Tareas</h1>
        <Button onClick={handleCreateTask}>
          <PlusIcon className="w-4 h-4 mr-2" />
          Nueva Tarea
        </Button>
      </div>

      {tasks.length === 0 ? (
        <div className="text-center py-8">
          <p className="text-gray-500">No hay tareas creadas aún.</p>
        </div>
      ) : (
        <div className="grid gap-4">
          {tasks.map((task: Task) => (
            <div
              key={task.id}
              className="p-4 border rounded-lg shadow-sm hover:shadow-md transition-shadow"
            >
              <h3 className="font-medium">{task.title}</h3>
              {/* Aquí irían más detalles de la tarea */}
            </div>
          ))}
        </div>
      )}

      <LoginDialog
        isOpen={isLoginDialogOpen}
        onClose={() => setIsLoginDialogOpen(false)}
        onLogin={handleLogin}
        onContinueOffline={() => {
          addTask({
            title: "Nueva tarea",
            startDate: new Date(),
          })
        }}
      />
    </div>
  )
} 