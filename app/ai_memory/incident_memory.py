from datetime import datetime


class IncidentMemory:

    def remember(self, incident):

        return {
            "type": "incident",
            "incident": incident,
            "patterns": [
                "Attack classification",
                "Previous response",
                "Investigation outcome"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }