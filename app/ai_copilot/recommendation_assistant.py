from datetime import datetime


class RecommendationAssistant:

    def recommend(self, incident):

        return {

            "recommendations": [
                "Isolate affected endpoint",
                "Block malicious indicators",
                "Reset compromised credentials",
                "Perform forensic investigation"
            ],

            "priority":
                "high",

            "timestamp":
                datetime.utcnow().isoformat()
        }