from datetime import datetime
import uuid


class MemoryStore:

    def __init__(self):
        self.memories = []

    def store(self, category, data):

        record = {
            "memory_id": f"MEM-{uuid.uuid4().hex[:8].upper()}",
            "category": category,
            "data": data,
            "created_at": datetime.utcnow().isoformat()
        }

        self.memories.append(record)

        return record


    def search(self, keyword):

        results = []

        for memory in self.memories:
            if keyword.lower() in str(memory).lower():
                results.append(memory)

        return results


    def all(self):

        return {
            "count": len(self.memories),
            "memories": self.memories
        }