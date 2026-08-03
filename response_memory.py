from datetime import datetime
import uuid


class ResponseMemory:

    def store(self, incident):

        return {
            "memory_id":
                "RESP-" + uuid.uuid4().hex[:8].upper(),

            "incident":
                incident,

            "stored": [
                "Incident lifecycle",
                "Response actions",
                "Recovery decisions",
                "Lessons learned"
            ],

            "timestamp":
                datetime.utcnow().isoformat()
        }