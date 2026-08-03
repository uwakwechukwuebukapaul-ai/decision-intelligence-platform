from datetime import datetime


class IdentityMemory:
    """
    Stores identity security events.
    """

    def __init__(self):
        self.records = []


    def store(self, event):

        record = {
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.records.append(record)

        return record


    def history(self):

        return {
            "records": self.records,
            "count": len(self.records)
        }