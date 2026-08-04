import uuid
from datetime import datetime


class WorkflowLogger:

    def record(self, incident):

        return {
            "log_id": f"SOARLOG-{uuid.uuid4().hex[:8].upper()}",
            "event": "SOAR workflow executed",
            "incident": incident,
            "timestamp": datetime.utcnow().isoformat()
        }