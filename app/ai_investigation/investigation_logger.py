import uuid
from datetime import datetime


class InvestigationLogger:

    def log(self, incident):

        return {
            "log_id":
                f"INVLOG-{uuid.uuid4().hex[:8].upper()}",
            "event":
                "AI investigation executed",
            "incident":
                incident,
            "timestamp":
                datetime.utcnow().isoformat()
        }