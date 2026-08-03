from datetime import datetime

from .event_normalizer import EventNormalizer
from .entity_correlator import EntityCorrelator
from .alert_correlator import AlertCorrelator
from .timeline_builder import TimelineBuilder
from .evidence_fusion import EvidenceFusion
from .risk_aggregator import RiskAggregator
from .fabric_memory import FabricMemory
from .fabric_logger import FabricLogger


class SecurityFabricEngine:

    def __init__(self):

        self.normalizer = EventNormalizer()
        self.entity = EntityCorrelator()
        self.alert = AlertCorrelator()
        self.timeline = TimelineBuilder()
        self.evidence = EvidenceFusion()
        self.risk = RiskAggregator()
        self.memory = FabricMemory()
        self.logger = FabricLogger()


    def correlate(self, event):

        normalized = self.normalizer.normalize(event)

        entities = self.entity.correlate(normalized)

        alerts = self.alert.correlate(
            normalized,
            entities
        )

        timeline = self.timeline.build(
            normalized,
            alerts
        )

        evidence = self.evidence.fuse(
            normalized,
            entities,
            alerts
        )

        risk = self.risk.calculate(
            alerts,
            evidence
        )

        memory = self.memory.store(event)

        log = self.logger.log(event)


        return {
            "status": "completed",
            "event": event,
            "normalized_event": normalized,
            "entities": entities,
            "alerts": alerts,
            "timeline": timeline,
            "evidence": evidence,
            "risk": risk,
            "memory": memory,
            "log": log,
            "created_at": datetime.utcnow().isoformat()
        }