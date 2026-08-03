from datetime import datetime


class SchemaNormalizer:
    """
    Converts events into Sentinel DNA unified schema.
    """


    def normalize(
        self,
        event
    ):

        return {

            "timestamp":
                datetime.utcnow().isoformat(),

            "source":
                event.get(
                    "source",
                    "unknown"
                ),

            "event_type":
                "security_event",

            "severity":
                "unknown",

            "asset":
                "unknown",

            "user":
                "unknown",

            "indicators":
                [],

            "raw_event":
                event.get(
                    "event"
                )

        }