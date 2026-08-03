from datetime import datetime


class FusionMemory:
    """
    Stores intelligence fusion history.
    """

    def __init__(self):

        self.memory = []


    def store(self, data):

        record = {
            "data": data,
            "created_at": datetime.utcnow().isoformat()
        }

        self.memory.append(record)

        return record


    def retrieve(self):

        return self.memory