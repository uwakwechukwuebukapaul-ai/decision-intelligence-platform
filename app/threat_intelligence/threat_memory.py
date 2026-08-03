from datetime import datetime
import uuid


class ThreatMemory:


    def store(self, event):

        return {

            "memory_id":
                "THREAT-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                event,

            "learned":
                [
                    "Threat behavior",
                    "IOC intelligence",
                    "Attack pattern"
                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }