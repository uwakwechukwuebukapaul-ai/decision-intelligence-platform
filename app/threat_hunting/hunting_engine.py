from datetime import datetime

from .query_builder import QueryBuilder
from .behavior_hunter import BehaviorHunter
from .ioc_hunter import IOCHunter
from .attack_path_analyzer import AttackPathAnalyzer
from .hypothesis_engine import HypothesisEngine
from .hunt_memory import HuntMemory
from .hunt_logger import HuntLogger


class ThreatHuntingEngine:


    def __init__(self):

        self.query_builder = QueryBuilder()
        self.behavior = BehaviorHunter()
        self.ioc = IOCHunter()
        self.attack_path = AttackPathAnalyzer()
        self.hypothesis = HypothesisEngine()
        self.memory = HuntMemory()
        self.logger = HuntLogger()


    def hunt(self, event):

        hypothesis = self.hypothesis.create(
            event
        )

        queries = self.query_builder.generate(
            event
        )

        behavior = self.behavior.analyze(
            event
        )

        ioc_matches = self.ioc.search(
            event
        )

        attack_paths = self.attack_path.analyze(
            event
        )

        memory = self.memory.store(
            event
        )

        log = self.logger.record(
            event
        )


        return {

            "status": "completed",

            "hunt_type":
                "AI Threat Hunt",

            "event":
                event,

            "hypothesis":
                hypothesis,

            "queries_generated":
                queries,

            "behavior_analysis":
                behavior,

            "ioc_matches":
                ioc_matches,

            "attack_paths":
                attack_paths,

            "memory":
                memory,

            "log":
                log,

            "risk":
                "critical"
                if "ransomware" in event.lower()
                else "medium",

            "created_at":
                datetime.utcnow().isoformat()

        }