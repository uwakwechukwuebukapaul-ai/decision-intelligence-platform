from datetime import datetime


class CommunicationManager:

    def notify(self, incident):

        return {
            "incident": incident,
            "notifications": [
                "SOC Team",
                "Security Leadership",
                "Incident Stakeholders"
            ],
            "status": "communication_sent",
            "timestamp": datetime.utcnow().isoformat()
        }