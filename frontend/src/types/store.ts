import { Task, CreateTaskDTO } from './task';

export interface TaskStore {
  tasks: Task[];
  isOfflineMode: boolean;
  setOfflineMode: (mode: boolean) => void;
  addTask: (task: CreateTaskDTO) => void;
  toggleTaskComplete: (taskId: string) => void;
  addSubTask: (taskId: string, title: string) => void;
  toggleSubTaskComplete: (taskId: string, subTaskId: string) => void;
  deleteTask: (taskId: string) => void;
} 