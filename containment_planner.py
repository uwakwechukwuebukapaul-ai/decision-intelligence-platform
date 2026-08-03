from datetime import datetime


class ContainmentPlanner:

    def plan(self, incident):

        return {
            "containment_actions": [
                "Isolate affected systems",
                "Block malicious indicators",
                "Disable compromised accounts",
                "Restrict network access"
            ],
            "status": "planned",
            "timestamp": datetime.utcnow().isoformat()
        }