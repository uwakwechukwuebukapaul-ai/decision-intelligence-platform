from datetime import datetime

from .rule_manager import RuleManager
from .rule_generator import RuleGenerator
from .behavior_detector import BehaviorDetector
from .sigma_mapper import SigmaMapper
from .alert_tuner import AlertTuner
from .detection_memory import DetectionMemory
from .detection_logger import DetectionLogger


class DetectionEngine:

    def __init__(self):
        self.rules = RuleManager()
        self.generator = RuleGenerator()
        self.behavior = BehaviorDetector()
        self.sigma = SigmaMapper()
        self.tuner = AlertTuner()
        self.memory = DetectionMemory()
        self.logger = DetectionLogger()


    def detect(self, event):

        behavior = self.behavior.analyze(event)

        rules = self.rules.match(event)

        generated = self.generator.generate(event)

        sigma = self.sigma.map(event)

        tuning = self.tuner.optimize(event)


        result = {

            "status": "completed",

            "event": event,

            "behavior_analysis": behavior,

            "matched_rules": rules,

            "generated_detection": generated,

            "sigma_mapping": sigma,

            "alert_tuning": tuning,

            "memory": self.memory.store(event),

            "log": self.logger.record(event),

            "created_at": datetime.utcnow().isoformat()

        }


        return result