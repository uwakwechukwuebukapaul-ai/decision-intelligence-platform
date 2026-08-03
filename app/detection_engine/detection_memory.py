from datetime import datetime
import uuid


class DetectionMemory:


    def store(self, event):

        return {

            "memory_id":
                "DET-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                event,

            "stored_patterns":
                [
                    "Detection rule",
                    "Attack behavior",
                    "MITRE mapping"
                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }