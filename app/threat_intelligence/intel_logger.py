from datetime import datetime
import uuid


class IntelLogger:


    def __init__(self):

        self.logs = []


    def log(self, threat):

        record = {

            "log_id":
            f"INTLOG-{uuid.uuid4().hex[:8].upper()}",

            "event":
            "Threat intelligence analysis executed",

            "data":
            threat,

            "timestamp":
            datetime.utcnow().isoformat()
        }


        self.logs.append(record)

        return record