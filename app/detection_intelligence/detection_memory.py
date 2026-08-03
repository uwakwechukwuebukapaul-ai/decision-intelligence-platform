from datetime import datetime
import uuid


class DetectionMemory:
    """
    Stores detection intelligence learning history.
    Future expansion:
    - Vector database integration
    - Threat pattern learning
    - Detection tuning memory
    """

    def __init__(self):
        self.memory = []

    def store(self, data):
        memory_id = f"DETECT-{uuid.uuid4().hex[:8].upper()}"

        record = {
            "memory_id": memory_id,
            "data": data,
            "stored_items": [
                "Detection patterns",
                "Generated rules",
                "Threat intelligence"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }

        self.memory.append(record)

        return record


    def retrieve(self):
        return self.memory


    def clear(self):
        self.memory = []

        return {
            "status": "cleared",
            "timestamp": datetime.utcnow().isoformat()
        }