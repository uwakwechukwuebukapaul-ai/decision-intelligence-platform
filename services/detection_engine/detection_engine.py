from .pattern_detector import PatternDetector
from .rule_generator import RuleGenerator
from .sigma_mapper import SigmaMapper
from .detection_logger import DetectionLogger


class DetectionEngine:

    def __init__(self):
        self.pattern_detector = PatternDetector()
        self.rule_generator = RuleGenerator()
        self.sigma_mapper = SigmaMapper()
        self.logger = DetectionLogger()

    def analyze(self, event):

        patterns = self.pattern_detector.detect(event)

        rules = self.rule_generator.generate(patterns)

        sigma = self.sigma_mapper.map(patterns)

        result = {
            "event": event,
            "patterns": patterns,
            "rules": rules,
            "sigma": sigma,
            "status": "detection_processed"
        }

        self.logger.log(result)

        return result