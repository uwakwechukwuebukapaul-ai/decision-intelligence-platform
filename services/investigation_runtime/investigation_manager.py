from datetime import datetime


class InvestigationManager:

    def start(self, context):

        return {
            "investigation_status": "started",
            "context_id": context["context_id"],
            "event": context["event"],
            "timestamp": datetime.utcnow().isoformat()
        }