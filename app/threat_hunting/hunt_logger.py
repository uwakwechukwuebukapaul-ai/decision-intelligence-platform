from datetime import datetime
import uuid


class HuntLogger:


    def record(self, event):

        return {

            "log_id":
                "HUNTLOG-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                "Threat hunting executed",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }