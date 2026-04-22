from datetime import datetime

from sqlmodel import SQLModel, Field

from app.schemas.task import TaskStatus


class Task(SQLModel, table=True):
    __tablename__ = "tasks"

    id: int = Field(default=None, primary_key=True)
    title: str = Field(default=None, nullable=False)
    description: str = Field(default=None, nullable=True)
    status: TaskStatus = Field(default=TaskStatus.ACTIVE, nullable=False)
    created_at: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    updated_at: datetime = Field(default=None, nullable=True)
