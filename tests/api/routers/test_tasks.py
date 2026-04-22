import unittest
from datetime import datetime
from unittest.mock import Mock

from fastapi import HTTPException
from starlette.testclient import TestClient

from app.dependencies.task import get_task_service
from app.main import app
from app.schemas.task import Task, TaskList, TaskStatus


class TestTaskRoutes(unittest.TestCase):
    def setUp(self) -> None:
        self.service = Mock()
        app.dependency_overrides[get_task_service] = lambda: self.service
        self.client = TestClient(app)

    def tearDown(self) -> None:
        app.dependency_overrides.clear()
        self.client.close()

    @staticmethod
    def build_task(
        task_id: int = 1,
        title: str = "Task title",
        description: str = "Task description",
        status: TaskStatus = TaskStatus.ACTIVE,
    ) -> Task:
        return Task(
            id=task_id,
            title=title,
            description=description,
            status=status,
            created_at=datetime(2026, 4, 22, 10, 0, 0),
            updated_at=None,
        )

    def assert_task_payload(self, payload: dict, task: Task) -> None:
        self.assertEqual(payload["id"], task.id)
        self.assertEqual(payload["title"], task.title)
        self.assertEqual(payload["description"], task.description)
        self.assertEqual(payload["status"], task.status.value)
        self.assertIn("created_at", payload)
        self.assertIn("updated_at", payload)

    def test_create_task(self) -> None:
        task = self.build_task()
        self.service.create_task.return_value = task

        payload = {"title": "title 1", "description": "description 1"}
        response = self.client.post("/todos/", json=payload)

        self.assertEqual(response.status_code, 201)
        self.assert_task_payload(response.json(), task)
        self.service.create_task.assert_called_once()
        sent_task = self.service.create_task.call_args.args[0]
        self.assertEqual(sent_task.title, payload["title"])
        self.assertEqual(sent_task.description, payload["description"])
        self.assertEqual(sent_task.status, TaskStatus.ACTIVE)

    def test_create_task_returns_422_when_title_is_missing(self) -> None:
        response = self.client.post("/todos/", json={"description": "description 1"})

        self.assertEqual(response.status_code, 422)
        self.service.create_task.assert_not_called()

    def test_get_all_tasks_without_status_filter(self) -> None:
        tasks = [
            self.build_task(task_id=1, title="title 1"),
            self.build_task(task_id=2, title="title 2"),
        ]
        self.service.get_tasks.return_value = TaskList(data=tasks, page=1, limit=10, total=2)

        response = self.client.get("/todos/?page=1&limit=10")

        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertEqual(content["page"], 1)
        self.assertEqual(content["limit"], 10)
        self.assertEqual(content["total"], 2)
        self.assertEqual(len(content["data"]), 2)
        self.assertEqual(content["data"][0]["title"], "title 1")
        self.assertEqual(content["data"][1]["title"], "title 2")
        self.service.get_tasks.assert_called_once_with(page=1, limit=10, status=None)

    def test_get_tasks_with_status_filter(self) -> None:
        tasks = [
            self.build_task(task_id=2, title="done task", status=TaskStatus.COMPLETED),
        ]
        self.service.get_tasks.return_value = TaskList(data=tasks, page=1, limit=10, total=1)

        response = self.client.get("/todos/?page=1&limit=10&status=completed")

        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertEqual(content["total"], 1)
        self.assertEqual(len(content["data"]), 1)
        self.assertEqual(content["data"][0]["status"], TaskStatus.COMPLETED.value)
        self.service.get_tasks.assert_called_once_with(
            page=1,
            limit=10,
            status=TaskStatus.COMPLETED,
        )

    def test_get_task_by_id(self) -> None:
        task = self.build_task(task_id=3, title="specific task")
        self.service.get_task.return_value = task

        response = self.client.get("/todos/3")

        self.assertEqual(response.status_code, 200)
        self.assert_task_payload(response.json(), task)
        self.service.get_task.assert_called_once_with(3)

    def test_get_task_by_id_returns_404_when_missing(self) -> None:
        self.service.get_task.side_effect = HTTPException(status_code=404, detail="Task 99 not found")

        response = self.client.get("/todos/99")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {"detail": "Task 99 not found"})
        self.service.get_task.assert_called_once_with(99)

    def test_update_task(self) -> None:
        updated_task = self.build_task(
            task_id=4,
            title="updated title",
            description="updated description",
        )
        self.service.update_task_data.return_value = updated_task

        payload = {"title": "updated title", "description": "updated description"}
        response = self.client.put("/todos/4", json=payload)

        self.assertEqual(response.status_code, 200)
        self.assert_task_payload(response.json(), updated_task)
        self.service.update_task_data.assert_called_once()
        task_id, task_data = self.service.update_task_data.call_args.args
        self.assertEqual(task_id, 4)
        self.assertEqual(task_data.title, payload["title"])
        self.assertEqual(task_data.description, payload["description"])

    def test_change_status(self) -> None:
        task = self.build_task(task_id=5, status=TaskStatus.COMPLETED)
        self.service.change_status.return_value = task

        response = self.client.patch("/todos/5?status=completed")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], TaskStatus.COMPLETED.value)
        self.service.change_status.assert_called_once_with(5, TaskStatus.COMPLETED)

    def test_change_status_returns_422_for_invalid_status(self) -> None:
        response = self.client.patch("/todos/5?status=invalid")

        self.assertEqual(response.status_code, 422)
        self.service.change_status.assert_not_called()

    def test_delete_task(self) -> None:
        response = self.client.delete("/todos/7")

        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.content, b"")
        self.service.delete_task.assert_called_once_with(task_id=7)


if __name__ == "__main__":
    unittest.main()
