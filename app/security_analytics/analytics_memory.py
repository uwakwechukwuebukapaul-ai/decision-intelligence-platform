from datetime import datetime
import uuid


class AnalyticsMemory:


    def store(self, event):

        return {

            "memory_id":
                f"ANALYTICS-{uuid.uuid4().hex[:8].upper()}",

            "event":
                event,

            "stored":

                [
                    "Risk history",
                    "Entity behavior",
                    "Attack predictions"
                ],

            "timestamp":
                datetime.utcnow().isoformat()

        }