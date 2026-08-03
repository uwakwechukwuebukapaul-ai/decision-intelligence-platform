from datetime import datetime
import uuid


class EventBus:


    def publish(self, event):

        return {

            "event_id":
            f"EVENT-{uuid.uuid4().hex[:8].upper()}",

            "event": event,

            "status": "published",

            "timestamp":
            datetime.utcnow().isoformat()
        }