import uuid
from datetime import datetime


class MITRELogger:

    def log(self, event):

        return {
            "log_id":
                f"MITRELOG-{uuid.uuid4().hex[:8].upper()}",
            "event":
                "MITRE ATT&CK analysis executed",
            "data":
                event,
            "timestamp":
                datetime.utcnow().isoformat()
        }