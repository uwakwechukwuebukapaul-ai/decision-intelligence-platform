from datetime import datetime
import uuid


class GraphMemory:

    def store(self, incident, relationships):

        return {
            "memory_id": f"GRAPH-{uuid.uuid4().hex[:8].upper()}",
            "incident": incident,
            "stored": [
                "Entities",
                "Relationships",
                "Attack Paths"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }