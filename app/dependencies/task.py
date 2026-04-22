from fastapi.params import Depends
from sqlalchemy.orm import Session

from app.cores.database import get_session
from app.repositories.task_repository import TaskRepository
from app.services.task_service import TaskService


def get_task_repository(db: Session = Depends(get_session)):
    return TaskRepository(db=db)


def get_task_service(repo: TaskRepository = Depends(get_task_repository)):
    return TaskService(repository=repo)