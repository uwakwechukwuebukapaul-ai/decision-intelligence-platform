class AgentTask:
    """
    Represents a security task assigned
    to an autonomous agent.
    """

    def __init__(
        self,
        task_type,
        objective,
        priority="medium"
    ):

        self.task_type = task_type
        self.objective = objective
        self.priority = priority


    def to_dict(self):

        return {
            "task_type": self.task_type,
            "objective": self.objective,
            "priority": self.priority,
            "status": "created"
        }