from datetime import datetime


class EvidenceParser:

    def parse(self, evidence):

        event = evidence.get("event", "")

        return {
            "raw_event": event,
            "normalized_event": event.lower(),
            "artifacts": [
                "Security Event",
                "Attack Behavior"
            ],
            "timestamp": datetime.utcnow().isoformat()
        }