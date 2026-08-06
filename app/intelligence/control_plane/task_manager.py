"""
Task Manager

Tracks intelligence execution tasks.
"""


from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any
import uuid



@dataclass
class IntelligenceTask:

    capability: str
    payload: dict[str, Any]

    task_id: str = field(
        default_factory=lambda:
        str(uuid.uuid4())
    )

    status: str = "created"

    created_at: str = field(
        default_factory=lambda:
        datetime.now(timezone.utc).isoformat()
    )


class TaskManager:

    def __init__(self):

        self.tasks = {}


    def create_task(
        self,
        capability: str,
        payload: dict,
    ):

        task = IntelligenceTask(
            capability=capability,
            payload=payload,
        )

        self.tasks[task.task_id] = task

        return task



    def update_status(
        self,
        task_id: str,
        status: str,
    ):

        task = self.tasks.get(task_id)

        if task is None:
            raise ValueError(
                "Task not found"
            )

        task.status = status

        return task



    def get_task(
        self,
        task_id: str,
    ):

        return self.tasks.get(task_id)