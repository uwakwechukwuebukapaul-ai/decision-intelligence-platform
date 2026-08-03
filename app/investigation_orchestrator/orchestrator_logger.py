import uuid
from datetime import datetime


class OrchestratorLogger:


    def log(self, event):

        return {

            "log_id":
                "ORCHLOG-"
                + uuid.uuid4().hex[:8].upper(),

            "event":
                "Investigation orchestration executed",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()
        }