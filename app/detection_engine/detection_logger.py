import uuid
from datetime import datetime


class DetectionLogger:


    def record(self,event):

        return {

            "log_id":
                "DETECTLOG-" + str(uuid.uuid4())[:8].upper(),

            "event":
                "Detection engine executed",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }