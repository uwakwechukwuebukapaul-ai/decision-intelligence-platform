import uuid
from datetime import datetime


class ReasoningMemory:


    def store(self, event):

        return {

            "memory_id":
                "REASON-"
                + uuid.uuid4().hex[:8].upper(),

            "event":
                event,

            "stored":
                [
                    "Threat reasoning",
                    "Risk decisions",
                    "Response decisions"
                ],

            "timestamp":
                datetime.utcnow().isoformat()
        }