import uuid

from .entity_correlator import EntityCorrelator
from .signal_fusion import SignalFusion
from .correlation_repository import CorrelationRepository
from .correlation_schema import CorrelationRecord, timestamp



class CorrelationEngine:


    def __init__(self):

        self.entity_correlator = EntityCorrelator()

        self.signal_fusion = SignalFusion()

        self.repository = CorrelationRepository()



    def correlate(self, data):


        entities = self.entity_correlator.correlate(
            data
        )


        risk = self.signal_fusion.calculate(
            data
        )


        record = CorrelationRecord(

            correlation_id=
            f"COR-{uuid.uuid4().hex[:8].upper()}",

            incident_id=
            data.get("incident_id"),

            entities=
            entities["entities"],

            relationships=
            entities["relationships"],

            risk_score=
            risk["risk_score"],

            confidence=0.97,

            created_at=
            timestamp()
        )


        self.repository.save(
            record.to_dict()
        )


        return {

            "correlation_id":
            record.correlation_id,

            "incident_id":
            record.incident_id,

            "entities":
            record.entities,

            "relationships":
            record.relationships,

            "risk_score":
            record.risk_score,

            "signals":
            risk["signals"],

            "confidence":
            record.confidence,

            "created_at":
            record.created_at
        }