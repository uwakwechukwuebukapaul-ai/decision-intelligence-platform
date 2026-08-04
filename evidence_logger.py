import uuid
from datetime import datetime


class EvidenceLogger:

    def log(self, event):

        return {
            "log_id":
                "EVIDLOG-" + uuid.uuid4().hex[:8].upper(),

            "event":
                "Evidence Intelligence Executed",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()
        }