import uuid
from datetime import datetime


class HuntMemory:

    def store(self, data):

        return {
            "memory_id": "HUNT-" + str(uuid.uuid4())[:8].upper(),
            "stored": [
                "Hunting Hypothesis",
                "Search Queries",
                "Threat Behavior"
            ],
            "data": data,
            "timestamp": datetime.now().isoformat()
        }