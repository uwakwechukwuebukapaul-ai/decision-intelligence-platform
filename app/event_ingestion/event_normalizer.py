from datetime import datetime


class EventNormalizer:


    def normalize(self, event):

        return {

            "normalized_event":
                event["event"],

            "format":
                "Sentinel DNA Common Event Format",

            "status":
                "normalized",

            "timestamp":
                datetime.utcnow().isoformat()

        }