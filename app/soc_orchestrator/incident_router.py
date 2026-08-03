from datetime import datetime


class IncidentRouter:

    def route(self, incident):

        return {
            "incident": incident,
            "assigned_team": "SOC Incident Response",
            "destination": [
                "Threat Intelligence",
                "Detection Engineering",
                "SOAR Automation"
            ],
            "timestamp": datetime.now().isoformat()
        }