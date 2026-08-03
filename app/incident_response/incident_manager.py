from datetime import datetime
import uuid


class IncidentManager:

    def create_incident(self, incident):

        return {
            "incident_id": f"INC-{uuid.uuid4().hex[:8].upper()}",
            "incident": incident,
            "status": "active",
            "created_at": datetime.utcnow().isoformat()
        }