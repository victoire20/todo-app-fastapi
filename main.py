from fastapi import FastAPI
from pydantic import BaseModel
from uuid import UUID
from enum import Enum
from datetime import datetime

app = FastAPI()

class TaskStatus(str, Enum):
    active = "active"
    description = "description"


class Task(BaseModel):
    id: UUID
    content: str
    status: TaskStatus
    created: datetime
    updated: datetime


@app.get('/{task}')
async def main(task: Task):
    return {"message": "Hello world"}