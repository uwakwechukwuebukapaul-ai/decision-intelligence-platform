import uuid
from datetime import datetime, timezone


class FabricLogger:


    def log(self, event, data):

        return {

            "log_id":
                f"FABRIC-{uuid.uuid4().hex[:8].upper()}",

            "event": event,

            "data": data,

            "timestamp":
                datetime.now(timezone.utc).isoformat()

        }