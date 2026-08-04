from datetime import datetime
from .query_generator import QueryGenerator
from .behavior_hunter import BehaviorHunter
from .anomaly_detector import AnomalyDetector
from .hypothesis_engine import HypothesisEngine
from .hunt_scheduler import HuntScheduler
from .hunt_memory import HuntMemory
from .hunt_logger import HuntLogger


class ThreatHuntingEngine:

    def __init__(self):
        self.query_generator = QueryGenerator()
        self.behavior_hunter = BehaviorHunter()
        self.anomaly_detector = AnomalyDetector()
        self.hypothesis_engine = HypothesisEngine()
        self.scheduler = HuntScheduler()
        self.memory = HuntMemory()
        self.logger = HuntLogger()

    def hunt(self, event):

        hypothesis = self.hypothesis_engine.create(event)

        queries = self.query_generator.generate(event)

        behaviors = self.behavior_hunter.analyze(event)

        anomalies = self.anomaly_detector.detect(event)

        schedule = self.scheduler.create(hypothesis)

        memory = self.memory.store({
            "event": event,
            "hypothesis": hypothesis
        })

        log = self.logger.record(event)

        return {
            "status": "completed",
            "event": event,
            "hypothesis": hypothesis,
            "queries": queries,
            "behavior_analysis": behaviors,
            "anomalies": anomalies,
            "hunt_schedule": schedule,
            "memory": memory,
            "log": log,
            "created_at": datetime.now().isoformat()
        }