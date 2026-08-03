from datetime import datetime


class ControlAssessor:

    def assess(self, incident):

        return {
            "incident": incident,
            "controls": [
                "Detection controls",
                "Response controls",
                "Recovery controls"
            ],
            "assessment": "compliant",
            "score": 90,
            "timestamp": datetime.utcnow().isoformat()
        }