from datetime import datetime

from .technique_mapper import TechniqueMapper
from .tactic_analyzer import TacticAnalyzer
from .group_tracker import GroupTracker
from .software_tracker import SoftwareTracker
from .attack_navigator import AttackNavigator
from .coverage_analyzer import CoverageAnalyzer
from .mitre_memory import MITREMemory


class MITREIntelligenceEngine:

    def __init__(self):
        self.technique_mapper = TechniqueMapper()
        self.tactic_analyzer = TacticAnalyzer()
        self.group_tracker = GroupTracker()
        self.software_tracker = SoftwareTracker()
        self.navigator = AttackNavigator()
        self.coverage = CoverageAnalyzer()
        self.memory = MITREMemory()


    def analyze(self, incident):

        techniques = self.technique_mapper.map(incident)

        tactics = self.tactic_analyzer.analyze(
            techniques
        )

        groups = self.group_tracker.identify(
            incident
        )

        software = self.software_tracker.identify(
            incident
        )

        navigator = self.navigator.build(
            techniques
        )

        coverage = self.coverage.analyze(
            techniques
        )

        result = {
            "status": "completed",
            "incident": incident,
            "techniques": techniques,
            "tactics": tactics,
            "groups": groups,
            "software": software,
            "navigator": navigator,
            "coverage": coverage,
            "created_at": datetime.now().isoformat()
        }

        self.memory.store(result)

        return result