class AgentTaskManager:
    """
    Controls autonomous agent task lifecycle.
    """

    def __init__(self):

        self.tasks = []


    def create_task(
        self,
        agent,
        task,
        priority="medium"
    ):

        item = {

            "agent": agent,
            "task": task,
            "priority": priority,
            "status": "queued"

        }

        self.tasks.append(item)

        return item


    def assign_task(self, task_index):

        self.tasks[task_index]["status"] = "assigned"

        return self.tasks[task_index]


    def complete_task(self, task_index):

        self.tasks[task_index]["status"] = "completed"

        return self.tasks[task_index]


    def get_tasks(self):

        return self.tasks