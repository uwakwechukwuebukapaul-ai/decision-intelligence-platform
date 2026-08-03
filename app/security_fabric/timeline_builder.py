from datetime import datetime


class TimelineBuilder:


    def build(self, event, alert):

        return {
            "timeline": [
                "Security event received",
                "Event normalized",
                "Entities extracted",
                "Alert correlation completed",
                "Risk evaluated"
            ],
            "status": "generated",
            "timestamp": datetime.utcnow().isoformat()
        }