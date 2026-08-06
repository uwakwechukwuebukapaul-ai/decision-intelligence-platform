import uuid
from .intel_schema import ThreatIntelRecord, create_timestamp


class IOCManager:

    def create_ioc(
        self,
        indicator,
        indicator_type="domain",
        threat_type="malware",
        confidence=0.9,
        severity="high",
        source="internal_analysis"
    ):

        return ThreatIntelRecord(
            intel_id=f"IOC-{uuid.uuid4().hex[:8].upper()}",
            indicator=indicator,
            indicator_type=indicator_type,
            threat_type=threat_type,
            confidence=confidence,
            severity=severity,
            source=source,
            created_at=create_timestamp()
        ).to_dict()


    def enrich(self, indicator):

        return {
            "indicator": indicator,
            "reputation": "malicious",
            "categories": [
                "malware",
                "command_and_control"
            ],
            "confidence": 0.9
        }