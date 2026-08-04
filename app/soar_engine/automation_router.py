from datetime import datetime


class AutomationRouter:

    def route(self, incident):

        return {
            "workflow": [
                "Detection",
                "Investigation",
                "Containment",
                "Recovery"
            ],
            "incident": incident,
            "status": "routed",
            "timestamp": datetime.utcnow().isoformat()
        }