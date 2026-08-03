from datetime import datetime
import uuid


class SaaSLogger:

    def log(self, event):

        return {
            "log_id": f"SAASLOG-{uuid.uuid4().hex[:8].upper()}",
            "event": event,
            "timestamp": datetime.utcnow().isoformat()
        }