from datetime import datetime


class EradicationPlanner:

    def plan(self, incident):

        return {
            "eradication_actions": [
                "Remove malware",
                "Delete persistence mechanisms",
                "Patch vulnerabilities",
                "Reset compromised credentials"
            ],
            "status": "planned",
            "timestamp": datetime.utcnow().isoformat()
        }