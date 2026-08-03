from datetime import datetime

from .rule_generator import RuleGenerator
from .sigma_engine import SigmaEngine
from .query_builder import QueryBuilder
from .rule_validator import RuleValidator
from .coverage_analyzer import CoverageAnalyzer
from .threat_mapping import ThreatMapping
from .detection_memory import DetectionMemory


class DetectionEngine:

    def __init__(self):
        self.rule_generator = RuleGenerator()
        self.sigma_engine = SigmaEngine()
        self.query_builder = QueryBuilder()
        self.validator = RuleValidator()
        self.coverage = CoverageAnalyzer()
        self.mapping = ThreatMapping()
        self.memory = DetectionMemory()

    def create_detection(self, threat):

        rule = self.rule_generator.generate(threat)

        sigma = self.sigma_engine.create(rule)

        query = self.query_builder.build(threat)

        validation = self.validator.validate(rule)

        mapping = self.mapping.map(threat)

        coverage = self.coverage.analyze(mapping)

        self.memory.store(threat)

        return {
            "status": "completed",
            "threat": threat,
            "rule": rule,
            "sigma": sigma,
            "query": query,
            "validation": validation,
            "mitre_mapping": mapping,
            "coverage": coverage,
            "created_at": datetime.utcnow().isoformat()
        }