from datetime import datetime
import uuid


class ComplianceLogger:

    def log(self, incident):

        return {
            "log_id": f"COMPLOG-{uuid.uuid4().hex[:8].upper()}",
            "event": "Compliance analysis executed",
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }