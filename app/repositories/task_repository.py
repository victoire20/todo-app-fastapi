from datetime import datetime

from sqlalchemy.orm import Session
from sqlmodel import select

from app.models.task import Task as TaskModel
from app.schemas.task import TaskCreate, Task, TaskList, TaskStatus, TaskUpdate


class TaskRepository:
    def __init__(self, db: Session) -> None:
        self.db = db

    def create(self, data: TaskCreate) -> Task:
        task = TaskModel(**data.model_dump())

        self.db.add(task)
        self.db.commit()
        self.db.refresh(task)

        return task

    def get_tasks(self, status: TaskStatus | None, page: int = 1, limit: int = 10) -> TaskList:
        statement = select(TaskModel)

        if status is not None:
            statement = statement.where(TaskModel.status == status)

        total = len(self.db.exec(statement).all())

        data = (
            self.db.exec(
                statement.offset((page - 1) * limit).limit(limit)
            ).all()
        )

        return TaskList(
            data=data,
            page=page,
            limit=limit,
            total=total
        )

    def get_task(self, task_id: int) -> Task | None:
        return self.db.get(TaskModel, task_id)

    def update_task(self, old_data: Task, new_data: TaskUpdate) -> Task:
        for key, value in new_data.model_dump(exclude_unset=True).items():
            setattr(old_data, key, value)

        old_data.updated_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(old_data)

        return old_data

    def update_status(self, old_data: Task, new_status: TaskStatus) -> Task:
        old_data.status = new_status
        old_data.updated_at = datetime.utcnow()

        self.db.commit()
        self.db.refresh(old_data)

        return old_data

    def delete_task(self, task_id: int):
        task = self.db.get(TaskModel, task_id)
        if task:
            self.db.delete(task)
            self.db.commit()