from datetime import datetime


class TimelineReconstructor:

    def reconstruct(self, incident):

        return {
            "incident": incident,
            "timeline": [
                "Initial detection",
                "Initial access",
                "Execution",
                "Impact",
                "Response"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }