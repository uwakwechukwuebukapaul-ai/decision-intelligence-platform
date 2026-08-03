from datetime import datetime
import uuid


class ThreatLogger:


    def record(self, event):

        return {

            "log_id":
                "THREATLOG-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                "Threat intelligence analysis",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }