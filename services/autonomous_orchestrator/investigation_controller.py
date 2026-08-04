import datetime


class InvestigationController:


    def control(self, event):

        return {
            "phase": [
                "Evidence Collection",
                "Threat Analysis",
                "Context Building",
                "Investigation Reasoning"
            ],
            "event": event,
            "status": "controlled",
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat()
        }
