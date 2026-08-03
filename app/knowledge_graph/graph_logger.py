from datetime import datetime
import uuid


class GraphLogger:


    def record(self,event):

        return {

            "log_id":
                f"GRAPHLOG-{uuid.uuid4().hex[:8].upper()}",

            "event":
                "Knowledge graph generated",

            "data":
                event,

            "timestamp":
                datetime.utcnow().isoformat()

        }