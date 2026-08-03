from datetime import datetime


class ResponseOrchestrator:

    def orchestrate(self, incident):

        return {
            "response": [
                "Contain threat",
                "Investigate compromise",
                "Recover affected assets"
            ],
            "incident": incident,
            "status": "orchestrated",
            "timestamp": datetime.utcnow().isoformat()
        }