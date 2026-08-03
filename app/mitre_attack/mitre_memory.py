import uuid
from datetime import datetime


class MITREMemory:

    def store(self, event):

        return {
            "memory_id":
                f"MITRE-{uuid.uuid4().hex[:8].upper()}",
            "event":
                event,
            "stored":
                [
                    "Techniques",
                    "Tactics",
                    "Attack Paths"
                ],
            "timestamp":
                datetime.utcnow().isoformat()
        }