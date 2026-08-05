class AuditManager:
    """
    Enterprise audit tracking system.
    """

    def __init__(self):
        self.logs = []


    def record(self, action, actor="system"):

        event = {
            "actor": actor,
            "action": action
        }

        self.logs.append(event)

        return event


    def get_logs(self):

        return self.logs