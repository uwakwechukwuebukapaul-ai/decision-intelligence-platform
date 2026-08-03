from datetime import datetime


class ResponseManager:

    def prepare(self, incident):

        return {
            "incident": incident,
            "actions": [
                "Isolate affected assets",
                "Block malicious indicators",
                "Preserve forensic data",
                "Begin recovery process"
            ],
            "status": "READY",
            "timestamp": datetime.now().isoformat()
        }