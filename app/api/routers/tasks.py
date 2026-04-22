from typing import Annotated

from fastapi import APIRouter, Query
from fastapi.params import Depends

from app.dependencies.task import get_task_service
from app.schemas.task import TaskList, Task, TaskCreate, TaskUpdate, TaskStatus
from app.services.task_service import TaskService

router = APIRouter(tags=["tasks"], prefix="/todos")


@router.post("/", status_code=201, response_model=Task)
async def create_task(task: TaskCreate, service: TaskService = Depends(get_task_service)) -> Task:
    return service.create_task(task)

@router.get("/", status_code=200, response_model=TaskList)
async def get_tasks(
    page: Annotated[int, Query(description='Current page number')] = 1,
    limit: Annotated[int, Query(description='The maximum number of tasks to display')] = 10,
    status: Annotated[TaskStatus | None, Query(description="Task status")] = None,
    service: TaskService = Depends(get_task_service)
) -> TaskList:
    return service.get_tasks(page=page, limit=limit, status=status)

@router.get("/{task_id}", status_code=200, response_model=Task)
async def get_task(task_id: int, session: TaskService = Depends(get_task_service)) -> Task:
    return session.get_task(task_id)

@router.put("/{task_id}", status_code=200, response_model=Task)
async def update_task(task_id: int, task: TaskUpdate, session: TaskService = Depends(get_task_service)) -> Task:
    return session.update_task_data(task_id, task)

@router.patch("/{task_id}")
async def change_status(task_id: int, status: TaskStatus, session: TaskService = Depends(get_task_service)) -> Task:
    return session.change_status(task_id, status)

@router.delete("/{task_id}", status_code=204)
async def delete_task(task_id: int, session: TaskService = Depends(get_task_service)):
    session.delete_task(task_id=task_id)
