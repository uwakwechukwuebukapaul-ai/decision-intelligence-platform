import uuid

from .ioc_manager import IOCManager
from .feed_connector import FeedConnector
from .intel_repository import IntelRepository


class ThreatEngine:

    def __init__(self):

        self.ioc_manager = IOCManager()
        self.feed_connector = FeedConnector()
        self.repository = IntelRepository()


    def analyze(self, indicator):

        enrichment = self.ioc_manager.enrich(indicator)

        severity = "critical" if enrichment["reputation"] == "malicious" else "low"

        record = self.ioc_manager.create_ioc(
            indicator=indicator,
            severity=severity
        )

        self.repository.save(record)

        return {
            "threat_id": f"THREAT-{uuid.uuid4().hex[:8].upper()}",
            "indicator": indicator,
            "reputation": enrichment["reputation"],
            "severity": severity,
            "confidence": enrichment["confidence"],
            "categories": enrichment["categories"],
            "intel_record": record,
            "created_at": record["created_at"]
        }