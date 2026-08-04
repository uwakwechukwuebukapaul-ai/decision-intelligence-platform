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

        rules = self.rule_generator.generate(
            patterns
        )

        sigma_rules = self.sigma_mapper.map(
            rules
        )

        return {

            "event": event,

            "patterns": patterns,

            "rules": rules,

            "sigma": sigma_rules,

            "status":
                "detection_processed",

            "log":
                self.logger.log(
                    "Detection analysis completed"
                )
        }


    def detect(self, event):

        result = self.analyze(event)

        return {

            "event": event,

            "patterns":
                result.get(
                    "patterns",
                    []
                ),

            "rules":
                result.get(
                    "rules",
                    []
                ),

            "sigma":
                result.get(
                    "sigma",
                    []
                ),

            "status":
                "detection_processed"
        }