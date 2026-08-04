import uuid
from datetime import datetime


class HuntLogger:

    def record(self, event):

        return {
            "log_id": "HUNTLOG-" + str(uuid.uuid4())[:8].upper(),
            "event": "Threat hunting executed",
            "data": event,
            "timestamp": datetime.now().isoformat()
        }