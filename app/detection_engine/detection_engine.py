from datetime import datetime

from .rule_manager import RuleManager
from .alert_correlator import AlertCorrelator
from .behavior_analyzer import BehaviorAnalyzer
from .signature_engine import SignatureEngine
from .anomaly_detector import AnomalyDetector
from .sigma_engine import SigmaEngine


class DetectionEngine:

    def __init__(self):
        self.rules = RuleManager()
        self.correlator = AlertCorrelator()
        self.behavior = BehaviorAnalyzer()
        self.signature = SignatureEngine()
        self.anomaly = AnomalyDetector()
        self.sigma = SigmaEngine()


    def analyze(self, event):

        result = {

            "event": event,

            "rules": self.rules.evaluate(event),

            "behavior_analysis": self.behavior.analyze(event),

            "signature_analysis": self.signature.detect(event),

            "anomaly_analysis": self.anomaly.detect(event),

            "sigma_detection": self.sigma.evaluate(event),

        }


        result["correlation"] = self.correlator.correlate(result)


        result["status"] = "completed"

        result["timestamp"] = datetime.utcnow().isoformat()


        return result