from datetime import datetime

from .technique_mapper import TechniqueMapper
from .tactic_mapper import TacticMapper
from .group_tracker import GroupTracker
from .software_mapper import SoftwareMapper
from .attack_navigator import AttackNavigator
from .coverage_analyzer import CoverageAnalyzer
from .mitre_memory import MITREMemory
from .mitre_logger import MITRELogger


class MITREAttackEngine:

    def __init__(self):

        self.technique_mapper = TechniqueMapper()
        self.tactic_mapper = TacticMapper()
        self.group_tracker = GroupTracker()
        self.software_mapper = SoftwareMapper()
        self.navigator = AttackNavigator()
        self.coverage = CoverageAnalyzer()
        self.memory = MITREMemory()
        self.logger = MITRELogger()


    def analyze(self, event):

        techniques = (
            self.technique_mapper.map(event)
        )

        tactics = (
            self.tactic_mapper.map(
                techniques["techniques"]
            )
        )

        groups = (
            self.group_tracker.track(event)
        )

        software = (
            self.software_mapper.map(event)
        )

        navigator = (
            self.navigator.generate(
                tactics["tactics"]
            )
        )

        coverage = (
            self.coverage.analyze(
                techniques["techniques"]
            )
        )

        memory = (
            self.memory.store(event)
        )

        log = (
            self.logger.log(event)
        )


        return {

            "status":
                "completed",

            "event":
                event,

            "techniques":
                techniques,

            "tactics":
                tactics,

            "groups":
                groups,

            "software":
                software,

            "navigator":
                navigator,

            "coverage":
                coverage,

            "memory":
                memory,

            "log":
                log,

            "created_at":
                datetime.utcnow().isoformat()
        }