from datetime import datetime
import uuid


class IngestionLogger:


    def record(self, event):

        return {

            "log_id":
                "INGLOG-" +
                str(uuid.uuid4())[:8].upper(),

            "event":
                "Security event ingested",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }