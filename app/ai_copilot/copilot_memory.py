import uuid
from datetime import datetime


class CopilotMemory:

    def store(self, conversation):

        return {

            "memory_id":
                "COPILOT-"
                + uuid.uuid4().hex[:8].upper(),

            "conversation":
                conversation,

            "stored":
                [
                    "Analyst queries",
                    "Investigation context",
                    "Security decisions"
                ],

            "timestamp":
                datetime.utcnow().isoformat()
        }