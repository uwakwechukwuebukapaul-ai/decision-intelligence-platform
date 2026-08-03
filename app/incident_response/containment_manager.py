from datetime import datetime


class ContainmentManager:

    def contain(self, incident):

        return {
            "incident": incident,
            "actions": [
                "Isolate affected assets",
                "Block malicious indicators",
                "Disable compromised accounts",
                "Prevent lateral movement"
            ],
            "status": "CONTAINMENT_READY",
            "timestamp": datetime.utcnow().isoformat()
        }