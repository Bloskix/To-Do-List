import { create } from 'zustand';
import { persist } from 'zustand/middleware';
import { Task, CreateTaskDTO } from '@/types/task';
import { TaskStore } from '@/types/store';
import { v4 as uuidv4 } from 'uuid';

type State = {
  tasks: Task[];
  isOfflineMode: boolean;
}

type Actions = {
  setOfflineMode: (mode: boolean) => void;
  addTask: (task: CreateTaskDTO) => void;
  toggleTaskComplete: (taskId: string) => void;
  addSubTask: (taskId: string, title: string) => void;
  toggleSubTaskComplete: (taskId: string, subTaskId: string) => void;
  deleteTask: (taskId: string) => void;
}

export const useTaskStore = create<TaskStore>()(
  persist<State & Actions>(
    (set) => ({
      tasks: [],
      isOfflineMode: false,
      setOfflineMode: (mode: boolean) => set({ isOfflineMode: mode }),
      addTask: (taskData: CreateTaskDTO) =>
        set((state) => ({
          tasks: [
            ...state.tasks,
            {
              ...taskData,
              id: uuidv4(),
              completed: false,
              subtasks: [],
              createdAt: new Date(),
              updatedAt: new Date(),
            },
          ],
        })),
      toggleTaskComplete: (taskId: string) =>
        set((state) => ({
          tasks: state.tasks.map((task) =>
            task.id === taskId
              ? { ...task, completed: !task.completed, updatedAt: new Date() }
              : task
          ),
        })),
      addSubTask: (taskId: string, title: string) =>
        set((state) => ({
          tasks: state.tasks.map((task) =>
            task.id === taskId
              ? {
                  ...task,
                  subtasks: [
                    ...task.subtasks,
                    { id: uuidv4(), title, completed: false },
                  ],
                  updatedAt: new Date(),
                }
              : task
          ),
        })),
      toggleSubTaskComplete: (taskId: string, subTaskId: string) =>
        set((state) => ({
          tasks: state.tasks.map((task) =>
            task.id === taskId
              ? {
                  ...task,
                  subtasks: task.subtasks.map((subtask) =>
                    subtask.id === subTaskId
                      ? { ...subtask, completed: !subtask.completed }
                      : subtask
                  ),
                  updatedAt: new Date(),
                }
              : task
          ),
        })),
      deleteTask: (taskId: string) =>
        set((state) => ({
          tasks: state.tasks.filter((task) => task.id !== taskId),
        })),
    }),
    {
      name: 'task-storage',
    }
  )
); 