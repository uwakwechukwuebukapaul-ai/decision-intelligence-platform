from datetime import datetime
import uuid


class ResponseLogger:

    def record(self, incident):

        return {

            "log_id":
                "RESPLOG-" + uuid.uuid4().hex[:8].upper(),

            "event":
                "Incident response executed",

            "data":
                incident,

            "timestamp":
                datetime.utcnow().isoformat()
        }