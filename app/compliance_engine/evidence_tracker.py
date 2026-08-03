from datetime import datetime


class EvidenceTracker:

    def track(self, incident):

        return {
            "incident": incident,
            "evidence": [
                "Security logs",
                "Endpoint artifacts",
                "Network telemetry",
                "Investigation timeline"
            ],
            "status": "evidence_collected",
            "timestamp": datetime.utcnow().isoformat()
        }