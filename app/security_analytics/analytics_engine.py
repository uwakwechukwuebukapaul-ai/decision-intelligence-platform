from datetime import datetime

from .risk_scorer import RiskScorer
from .behavior_baseline import BehaviorBaseline
from .entity_scoring import EntityScoring
from .attack_prediction import AttackPrediction
from .security_metrics import SecurityMetrics
from .analytics_memory import AnalyticsMemory
from .analytics_logger import AnalyticsLogger


class SecurityAnalyticsEngine:

    def __init__(self):

        self.risk = RiskScorer()
        self.behavior = BehaviorBaseline()
        self.entity = EntityScoring()
        self.prediction = AttackPrediction()
        self.metrics = SecurityMetrics()
        self.memory = AnalyticsMemory()
        self.logger = AnalyticsLogger()


    def analyze(self, event):

        risk = self.risk.score(event)

        behavior = self.behavior.analyze(
            event
        )

        entity = self.entity.evaluate(
            event
        )

        prediction = self.prediction.predict(
            event
        )

        metrics = self.metrics.calculate(
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

            "event": event,

            "risk_analysis": risk,

            "behavior_baseline": behavior,

            "entity_analysis": entity,

            "attack_prediction": prediction,

            "security_metrics": metrics,

            "memory": memory,

            "log": log,

            "created_at":
                datetime.utcnow().isoformat()

        }