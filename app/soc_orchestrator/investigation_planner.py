from datetime import datetime


class InvestigationPlanner:

    def plan(self, incident):

        return {
            "incident": incident,
            "steps": [
                "Collect evidence",
                "Analyze indicators",
                "Review timeline",
                "Map MITRE ATT&CK",
                "Determine containment"
            ],
            "timestamp": datetime.now().isoformat()
        }