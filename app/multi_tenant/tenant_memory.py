from datetime import datetime


class TenantMemory:
    """
    Stores tenant events and configuration history.
    """

    def __init__(self):

        self.records = []


    def store(self, data):

        record = {
            "data": data,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.records.append(record)

        return record


    def get_history(self):

        return {
            "records": self.records,
            "count": len(self.records)
        }