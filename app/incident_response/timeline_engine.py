from datetime import datetime


class TimelineEngine:



    def build(self, alert):


        events = [

            "Threat detected",

            "Alert generated",

            "Investigation started",

            "Response workflow initiated"

        ]


        return {

            "events": events,

            "event_count": len(events),

            "timestamp":
                datetime.utcnow().isoformat()

        }