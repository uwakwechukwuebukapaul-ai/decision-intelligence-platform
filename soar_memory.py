import uuid
from datetime import datetime


class SOARMemory:

    def store(self, incident, actions):

        return {
            "memory_id": f"SOAR-{uuid.uuid4().hex[:8].upper()}",
            "incident": incident,
            "stored": [
                "Response actions",
                "Playbook execution",
                "Automation history"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }