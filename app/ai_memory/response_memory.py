from datetime import datetime


class ResponseMemory:

    def remember_response(self, response):

        return {
            "type": "response",
            "response": response,
            "successful_actions": [
                "Containment",
                "Eradication",
                "Recovery"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }