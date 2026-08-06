from datetime import datetime

from .learning_repository import LearningRepository
from .decision_optimizer import DecisionOptimizer


class LearningEngine:

    def __init__(self):
        self.repository = LearningRepository()
        self.optimizer = DecisionOptimizer()

    def learn(
        self,
        incident_id,
        indicator,
        previous_decision,
        confidence,
        patterns=None
    ):

        patterns = patterns or []

        optimization = self.optimizer.optimize(
            previous_decision,
            confidence,
            patterns
        )

        record = {
            "learning_id": self.repository.generate_id(),
            "incident_id": incident_id,
            "indicator": indicator,
            "previous_decision": previous_decision,
            "optimized_decision": optimization["optimized_decision"],
            "confidence": confidence,
            "improvement": optimization["improvement"],
            "patterns": patterns,
            "created_at": datetime.utcnow().isoformat()
        }

        return self.repository.save(record)