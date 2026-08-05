class ExecutionMonitor:
    """
    Tracks autonomous agent execution.
    """

    def __init__(self):

        self.history = []


    def record(
        self,
        agent,
        action,
        status
    ):

        event = {
            "agent": agent,
            "action": action,
            "status": status
        }

        self.history.append(event)

        return event


    def get_history(self):

        return self.history