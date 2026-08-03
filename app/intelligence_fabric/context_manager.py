from datetime import datetime
import uuid


class ContextManager:


    def create(self, event):

        return {

            "context_id":
            f"CTX-{uuid.uuid4().hex[:8].upper()}",

            "event": event,

            "context": [

                "Threat Context",
                "Asset Context",
                "Attack Context",
                "Response Context"

            ],

            "timestamp":
            datetime.utcnow().isoformat()
        }