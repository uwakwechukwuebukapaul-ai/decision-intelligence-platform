from datetime import datetime
import uuid


class SOARLogger:

    def log(self, incident):

        return {
            "log_id": "SOARLOG-" + uuid.uuid4().hex[:8].upper(),
            "event": "SOAR automation executed",
            "data": incident,
            "timestamp": datetime.utcnow().isoformat()
        }