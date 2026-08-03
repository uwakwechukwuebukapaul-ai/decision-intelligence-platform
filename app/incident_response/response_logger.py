from datetime import datetime
import uuid


class ResponseLogger:

    def log(self, incident):

        return {
            "log_id": f"RESPLOG-{uuid.uuid4().hex[:8].upper()}",
            "event": "Incident response executed",
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }