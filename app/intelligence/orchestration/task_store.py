"""
Sentinel DNA - Investigation Task Store
"""

from __future__ import annotations


class InvestigationTaskStore:


    def __init__(self):

        self.tasks = {}



    def save(
        self,
        task
    ):

        self.tasks[
            task.task_id
        ] = task


        return task



    def get(
        self,
        task_id
    ):

        return self.tasks.get(
            task_id
        )



    def all(self):

        return list(
            self.tasks.values()
        )