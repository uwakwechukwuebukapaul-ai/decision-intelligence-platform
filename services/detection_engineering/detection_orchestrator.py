from .rule_generator import RuleGenerator
from .pattern_analyzer import PatternAnalyzer
from .query_builder import QueryBuilder
from .rule_validator import RuleValidator
from .coverage_analyzer import CoverageAnalyzer


class DetectionOrchestrator:
    """
    Coordinates detection engineering workflow.
    """

    def __init__(self):

        self.pattern_analyzer = PatternAnalyzer()
        self.rule_generator = RuleGenerator()
        self.query_builder = QueryBuilder()
        self.validator = RuleValidator()
        self.coverage = CoverageAnalyzer()


    def create_detection(self, events):

        patterns = self.pattern_analyzer.analyze(
            events
        )

        rules = []

        techniques = []

        for pattern in patterns:

            rule = self.rule_generator.generate(
                {
                    "name": pattern["pattern"],
                    "behavior": pattern,
                    "severity": "high"
                }
            )

            rule["query"] = self.query_builder.build(
                pattern
            )

            rules.append(rule)

            techniques.append(
                pattern["technique"]
            )


        validation = [
            self.validator.validate(rule)
            for rule in rules
        ]


        return {
            "rules": rules,
            "validation": validation,
            "coverage":
                self.coverage.analyze(
                    techniques
                )
        }