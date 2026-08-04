import uuid
from datetime import datetime


class InvestigationContext:

    def create(self, event):

        return {
            "context_id": f"INVCTX-{uuid.uuid4().hex[:8].upper()}",
            "event": event,
            "created_at": datetime.utcnow().isoformat()
        }