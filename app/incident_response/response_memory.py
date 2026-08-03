from datetime import datetime
import uuid


class ResponseMemory:

    def store(self, incident):

        return {
            "memory_id": f"RESP-{uuid.uuid4().hex[:8].upper()}",
            "incident": incident,
            "stored": [
                "Response actions",
                "Containment history",
                "Recovery information"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }