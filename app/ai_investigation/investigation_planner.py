from datetime import datetime


class InvestigationPlanner:

    def create_plan(self, incident):

        return {
            "steps": [
                "Collect evidence",
                "Analyze indicators",
                "Map attack techniques",
                "Identify root cause",
                "Recommend response actions"
            ],
            "status": "planned",
            "timestamp": datetime.utcnow().isoformat()
        }