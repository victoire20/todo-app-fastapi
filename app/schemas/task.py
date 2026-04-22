from typing import List

from pydantic import BaseModel, Field, ConfigDict

from datetime import datetime
from enum import Enum


class TaskStatus(str, Enum):
    ACTIVE = "active"
    COMPLETED = "completed"


class TaskBase(BaseModel):
    title: str = Field(nullable=False, max_length=100, description='Task title', example='Housekeeping Day')


class TaskCreate(TaskBase):
    description: str = Field(
        nullable=True,
        max_length=500,
        description='To spend the whole day giving the house a thorough cleaning from top to bottom, inside and out!'
    )
    status: TaskStatus = Field(
        default=TaskStatus.ACTIVE,
        nullable=True,
        description='Show whether the task has been completed or not'
    )


class TaskUpdate(TaskBase):
    description: str = Field(nullable=True, max_length=500)


class Task(TaskBase):
    id: int
    title: str
    description: str
    status: TaskStatus
    created_at: datetime
    updated_at: datetime | None

    model_config = ConfigDict(
        from_attributes=True,
        json_encoders={datetime: lambda dt: dt.strftime("%d-%m-%Y %H:%M")}
    )


class TaskList(BaseModel):
    data: List[Task]
    page: int
    limit: int
    total: int

    model_config = ConfigDict(from_attributes=True)

