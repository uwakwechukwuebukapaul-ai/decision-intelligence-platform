from .posture_calculator import PostureCalculator
from .control_analyzer import ControlAnalyzer
from .posture_repository import PostureRepository
from .posture_schema import create_posture_record


class PostureEngine:

    def __init__(self):
        self.calculator = PostureCalculator()
        self.controls = ControlAnalyzer()
        self.repository = PostureRepository()

    def evaluate(self, organization, signals):

        posture = self.calculator.calculate(signals)

        controls = self.controls.analyze(signals)

        recommendations = []

        if posture["level"] in ["high", "critical"]:
            recommendations.extend([
                "Investigate active threats",
                "Reduce exposed assets",
                "Improve detection coverage"
            ])

        record = create_posture_record(
            organization,
            posture["score"],
            posture["level"],
            posture["findings"],
            recommendations
        )

        record["controls"] = controls

        return self.repository.save(record)