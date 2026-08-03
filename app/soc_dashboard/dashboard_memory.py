from datetime import datetime


class DashboardMemory:
    """
    Stores dashboard states and historical snapshots.
    """

    def __init__(self):
        self.history = []


    def store(self, data):

        record = {
            "snapshot": data,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.history.append(record)

        return record


    def recall(self):

        return {
            "records": self.history,
            "count": len(self.history)
        }