from datetime import datetime


class MemoryLayer:
    """
    Stores autonomous brain experiences.
    """

    def __init__(self):

        self.memory = []


    def remember(self, data):

        record = {
            "experience": data,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.memory.append(record)

        return record


    def recall(self):

        return self.memory