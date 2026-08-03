from datetime import datetime
import uuid


class InvestigationContext:

    def create(self, event):

        return {
            "investigation_id":
                "INV-"
                + uuid.uuid4().hex[:8].upper(),

            "event":
                event,

            "created_at":
                datetime.utcnow().isoformat()
        }