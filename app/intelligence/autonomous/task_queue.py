"""
Sentinel DNA - Autonomous Task Queue

Manages investigation workloads.

Supports:

- Priority execution
- Pending investigations
- Future distributed workers
"""


from __future__ import annotations


import uuid
from datetime import datetime, timezone



class TaskQueue:


    def __init__(self):

        self.tasks = []



    def add_task(
        self,
        indicator: str,
        priority: int = 50,
        task_type: str = "investigation",
    ):


        task = {

            "task_id":
                f"TASK-{uuid.uuid4().hex[:8].upper()}",

            "indicator": indicator,

            "task_type": task_type,

            "priority": priority,

            "status": "queued",

            "created_at":
                self.timestamp()

        }


        self.tasks.append(task)


        return task




    def next_task(self):

        queued = [

            t for t in self.tasks
            if t["status"] == "queued"

        ]


        if not queued:

            return None


        queued.sort(
            key=lambda x:x["priority"],
            reverse=True
        )


        task = queued[0]

        task["status"] = "processing"


        return task




    def list_tasks(self):

        return self.tasks




    def timestamp(self):

        return datetime.now(
            timezone.utc
        ).isoformat()