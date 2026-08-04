from datetime import datetime
import uuid


class EvidenceCollector:

    def collect(self, event):

        return {
            "evidence_id": f"EVID-{uuid.uuid4().hex[:8].upper()}",
            "event": event,
            "evidence_sources": [
                "Security Logs",
                "Endpoint Telemetry",
                "Network Events",
                "Threat Intelligence"
            ],
            "collection_status": "completed",
            "timestamp": datetime.utcnow().isoformat()
        }