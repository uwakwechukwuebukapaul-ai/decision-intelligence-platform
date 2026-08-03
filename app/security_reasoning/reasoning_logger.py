import uuid
from datetime import datetime


class ReasoningLogger:


    def log(self, event):

        return {

            "log_id":
                "REASONLOG-"
                + uuid.uuid4().hex[:8].upper(),

            "event":
                "Security reasoning executed",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()
        }