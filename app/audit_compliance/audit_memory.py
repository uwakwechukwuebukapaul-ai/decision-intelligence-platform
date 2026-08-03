from datetime import datetime


class AuditMemory:
    """
    Stores audit history and security events.
    """

    def __init__(self):

        self.events = []


    def store(self, event):

        record = {
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.events.append(record)

        return record


    def history(self):

        return {
            "events": self.events,
            "count": len(self.events)
        }