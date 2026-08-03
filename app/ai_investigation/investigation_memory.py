import uuid
from datetime import datetime


class InvestigationMemory:

    def store(self, incident):

        return {
            "memory_id":
                f"INV-{uuid.uuid4().hex[:8].upper()}",
            "incident": incident,
            "stored": [
                "Investigation findings",
                "Threat analysis",
                "Root cause"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }