import uuid
from datetime import datetime


class CopilotLogger:

    def log(self, query):

        return {

            "log_id":
                "COPILOTLOG-"
                + uuid.uuid4().hex[:8].upper(),

            "event":
                "AI Copilot interaction",

            "query":
                query,

            "timestamp":
                datetime.utcnow().isoformat()
        }