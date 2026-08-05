from .hypothesis_engine import HypothesisEngine
from .behavior_analyzer import BehaviorAnalyzer
from .ioc_hunter import IOCHunter
from .attack_pattern_detector import AttackPatternDetector


class HuntOrchestrator:
    """
    Coordinates autonomous hunting workflow.
    """

    def __init__(self):

        self.hypothesis_engine = HypothesisEngine()
        self.behavior_analyzer = BehaviorAnalyzer()
        self.ioc_hunter = IOCHunter()
        self.attack_detector = AttackPatternDetector()


    def run(self, hunt_request):

        hypotheses = self.hypothesis_engine.generate(
            hunt_request
        )

        behaviors = self.behavior_analyzer.analyze(
            hunt_request
        )

        iocs = self.extract_iocs(
            hunt_request
        )

        ioc_results = self.ioc_hunter.hunt(
            iocs
        )

        attack_patterns = self.attack_detector.detect(
            hunt_request
        )

        return {
            "status": "completed",
            "hypotheses": hypotheses,
            "behavior_findings": behaviors,
            "ioc_results": ioc_results,
            "attack_patterns": attack_patterns,
        }


    def extract_iocs(self, data):

        if isinstance(data, list):
            return data

        text = str(data)

        words = text.split()

        possible_iocs = []

        for word in words:

            if "." in word or "/" in word:
                possible_iocs.append(word)

        return possible_iocs