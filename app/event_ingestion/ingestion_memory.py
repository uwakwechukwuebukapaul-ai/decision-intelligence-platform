from datetime import datetime
import uuid


class IngestionMemory:


    def store(self, event):

        return {

            "memory_id":
                "ING-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                event,

            "stored":
                [
                    "Raw event",
                    "Normalized event",
                    "Source metadata"
                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }