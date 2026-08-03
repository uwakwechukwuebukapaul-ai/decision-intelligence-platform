from datetime import datetime
import uuid


class DetectionLogger:


    def record(self, event):

        return {

            "log_id":
                "DETLOG-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                "Detection executed",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }