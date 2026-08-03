import uuid
from datetime import datetime


class CopilotLogger:

    def log(self, incident):

        return {

            "log_id":
                f"COPLOG-{uuid.uuid4().hex[:8].upper()}",

            "event":
                "AI Copilot interaction",

            "incident":
                incident,

            "timestamp":
                datetime.utcnow().isoformat()
        }