import uuid

from .rule_engine import RuleEngine
from .correlation_engine import CorrelationEngine
from .detection_repository import DetectionRepository
from .detection_schema import Detection, timestamp



class DetectionEngine:


    def __init__(self):

        self.rules = RuleEngine()
        self.correlation = CorrelationEngine()
        self.repository = DetectionRepository()



    def detect(self, event):

        rules = self.rules.evaluate(event)

        signals = self.correlation.correlate(event)


        severity = (
            "critical"
            if event.get("severity") == "critical"
            else "high"
        )


        detection = Detection(

            detection_id=f"DET-{uuid.uuid4().hex[:8].upper()}",

            indicator=event.get("indicator"),

            rule=", ".join(rules),

            severity=severity,

            confidence=0.95,

            status="triggered",

            created_at=timestamp()

        )


        self.repository.save(
            detection.to_dict()
        )


        return {

            "detection_id": detection.detection_id,

            "indicator": detection.indicator,

            "severity": detection.severity,

            "rules": rules,

            "correlated_signals": signals,

            "confidence": detection.confidence,

            "status": detection.status,

            "created_at": detection.created_at
        }