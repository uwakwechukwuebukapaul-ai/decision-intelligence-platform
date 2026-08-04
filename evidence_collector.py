from datetime import datetime


class EvidenceCollector:

    def collect(self, event):

        return {
            "source": "Security Event Stream",
            "event": event,
            "evidence_types": [
                "Logs",
                "Network Activity",
                "Process Activity",
                "Threat Indicators"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }