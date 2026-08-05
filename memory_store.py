from datetime import datetime


class MemoryStore:

    def __init__(self):
        self.memories = []

    def save(self, memory):
        record = {
            "memory": memory,
            "timestamp": datetime.utcnow().isoformat()
        }

        self.memories.append(record)

        return record

    def all(self):
        return self.memories