from fastapi import HTTPException

from app.repositories.task_repository import TaskRepository
from app.schemas.task import TaskCreate, TaskStatus, TaskList, Task, TaskUpdate


class TaskService:
    def __init__(self, repository: TaskRepository) -> None:
        self.repo = repository

    def create_task(self, task_data: TaskCreate) -> Task:
        return self.repo.create(data=task_data)

    def get_tasks(self, page: int = 1, limit: int = 10, status: TaskStatus | None = None) -> TaskList:
        return self.repo.get_tasks(status=status, page=page, limit=limit)

    def get_task(self, task_id: int) -> Task:
        task = self.repo.get_task(task_id=task_id)
        if not task:
            raise HTTPException(status_code=404, detail=f"Task {task_id} not found")
        return task

    def update_task_data(self, task_id: int, task_data: TaskUpdate) -> Task:
        task = self.get_task(task_id=task_id)
        return self.repo.update_task(old_data=task, new_data=task_data)

    def change_status(self, task_id: int, status: TaskStatus) -> Task:
        task = self.get_task(task_id=task_id)
        return self.repo.update_status(old_data=task, new_status=status)

    def delete_task(self, task_id: int):
        self.get_task(task_id=task_id)
        self.repo.delete_task(task_id=task_id)
