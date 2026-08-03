from datetime import datetime


class ContainmentEngine:

    def contain(self, incident):

        return {
            "incident": incident,
            "actions": [
                "Isolate affected systems",
                "Disable compromised accounts",
                "Block malicious indicators"
            ],
            "status": "containment_completed",
            "timestamp": datetime.utcnow().isoformat()
        }