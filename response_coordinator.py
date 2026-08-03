from datetime import datetime


class ResponseCoordinator:

    def coordinate(self, incident):

        return {
            "response_flow": [
                "Detection",
                "Analysis",
                "Containment",
                "Eradication",
                "Recovery"
            ],
            "incident": incident,
            "status": "coordinated",
            "timestamp": datetime.utcnow().isoformat()
        }