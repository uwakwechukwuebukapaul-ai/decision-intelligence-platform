from datetime import datetime


class AnalystAssistant:

    def assist(self, incident):

        return {
            "assistant_response": [
                "Review affected assets",
                "Validate indicators",
                "Check authentication activity",
                "Confirm containment status"
            ],
            "role":
                "SOC Analyst Assistant",
            "timestamp":
                datetime.utcnow().isoformat()
        }