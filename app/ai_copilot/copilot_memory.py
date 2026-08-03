import uuid
from datetime import datetime


class CopilotMemory:

    def store(self, incident):

        return {

            "memory_id":
                f"COPILOT-{uuid.uuid4().hex[:8].upper()}",

            "incident":
                incident,

            "stored":
                [
                    "Analyst conversation",
                    "Investigation context",
                    "Recommendations"
                ],

            "timestamp":
                datetime.utcnow().isoformat()
        }