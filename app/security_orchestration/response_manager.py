from datetime import datetime


class ResponseManager:

    def prepare(self, event):

        return {
            "response_actions": [
                "Validate incident",
                "Contain affected assets",
                "Block indicators",
                "Collect forensic evidence",
                "Recover services"
            ],
            "event": event,
            "status": "ready",
            "timestamp": datetime.utcnow().isoformat()
        }