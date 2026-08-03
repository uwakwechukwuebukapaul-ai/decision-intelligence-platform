from datetime import datetime

from .rule_engine import RuleEngine
from .behavior_analyzer import BehaviorAnalyzer
from .signature_engine import SignatureEngine
from .correlation_engine import CorrelationEngine
from .alert_generator import AlertGenerator
from .mitre_mapper import MITREMapper
from .detection_memory import DetectionMemory
from .detection_logger import DetectionLogger


class DetectionEngine:

    def __init__(self):

        self.rules = RuleEngine()
        self.behavior = BehaviorAnalyzer()
        self.signature = SignatureEngine()
        self.correlation = CorrelationEngine()
        self.alert = AlertGenerator()
        self.mitre = MITREMapper()
        self.memory = DetectionMemory()
        self.logger = DetectionLogger()


    def detect(self, event):

        rule_result = self.rules.evaluate(event)

        behavior_result = self.behavior.analyze(event)

        signature_result = self.signature.match(event)

        correlation_result = self.correlation.correlate(
            event
        )

        mitre_result = self.mitre.map(
            event
        )

        alert_result = self.alert.generate(
            event,
            rule_result
        )

        memory_result = self.memory.store(
            event
        )

        log_result = self.logger.record(
            event
        )


        return {

            "status": "completed",

            "event": event,

            "rule_analysis": rule_result,

            "behavior_analysis": behavior_result,

            "signature_analysis": signature_result,

            "correlation": correlation_result,

            "mitre": mitre_result,

            "alert": alert_result,

            "memory": memory_result,

            "log": log_result,

            "created_at":
                datetime.utcnow().isoformat()

        }