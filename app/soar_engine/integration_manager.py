from datetime import datetime


class IntegrationManager:

    def connect(self, incident):

        return {
            "integrations": [
                "SIEM",
                "EDR",
                "Threat Intelligence",
                "Ticketing System"
            ],
            "incident": incident,
            "status": "connected",
            "timestamp": datetime.utcnow().isoformat()
        }