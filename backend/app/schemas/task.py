from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class SubtaskBase(BaseModel):
    title: str
    completed: bool = False

class SubtaskCreate(SubtaskBase):
    pass

class Subtask(SubtaskBase):
    id: int
    task_id: int

    class Config:
        from_attributes = True

class TaskBase(BaseModel):
    title: str
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    title: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    completed: Optional[bool] = None

class Task(TaskBase):
    id: int
    created_at: datetime
    user_id: int
    subtasks: List[Subtask] = []

    class Config:
        from_attributes = True 