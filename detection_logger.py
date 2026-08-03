import uuid
from datetime import datetime


class DetectionLogger:

    def log(self, threat):

        return {

            "log_id":
                f"DETLOG-{uuid.uuid4().hex[:8].upper()}",

            "event":
                "AI Detection Engineering Executed",

            "threat":
                threat,

            "timestamp":
                datetime.utcnow().isoformat()
        }