"use client"

import { useTaskStore } from "@/store/useTaskStore"
import {
  Dialog,
  DialogContent,
  DialogDescription,
  DialogFooter,
  DialogHeader,
  DialogTitle,
} from "@/components/ui/modal"
import { Button } from "@/components/ui/button"
import { TaskStore } from "@/types/store"

interface LoginDialogProps {
  isOpen: boolean
  onClose: () => void
  onLogin: () => void
  onContinueOffline: () => void
}

export function LoginDialog({
  isOpen,
  onClose,
  onLogin,
  onContinueOffline,
}: LoginDialogProps) {
  const setOfflineMode = useTaskStore((state: TaskStore) => state.setOfflineMode)

  const handleContinueOffline = () => {
    setOfflineMode(true)
    onContinueOffline()
    onClose()
  }

  return (
    <Dialog open={isOpen} onOpenChange={onClose}>
      <DialogContent>
        <DialogHeader>
          <DialogTitle>¿Deseas iniciar sesión?</DialogTitle>
          <DialogDescription>
            Si continúas sin iniciar sesión, tus tareas se guardarán localmente y
            no estarán disponibles en otros dispositivos.
          </DialogDescription>
        </DialogHeader>
        <DialogFooter className="flex justify-between sm:justify-between">
          <Button variant="outline" onClick={handleContinueOffline}>
            Continuar sin conexión
          </Button>
          <Button onClick={onLogin}>Iniciar sesión</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  )
} 