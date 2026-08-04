from datetime import datetime


class EvidenceParser:

    def parse(self, evidence):

        return {
            "parsed_evidence": evidence,
            "format": "normalized_security_event",
            "fields": [
                "timestamp",
                "source",
                "event_type",
                "indicator",
                "behavior"
            ],
            "status": "parsed",
            "timestamp": datetime.utcnow().isoformat()
        }