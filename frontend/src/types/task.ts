export interface Task {
  id: string;
  title: string;
  completed: boolean;
  startDate?: Date;
  endDate?: Date;
  subtasks: SubTask[];
  createdAt: Date;
  updatedAt: Date;
}

export interface SubTask {
  id: string;
  title: string;
  completed: boolean;
}

export interface CreateTaskDTO {
  title: string;
  startDate?: Date;
  endDate?: Date;
} 