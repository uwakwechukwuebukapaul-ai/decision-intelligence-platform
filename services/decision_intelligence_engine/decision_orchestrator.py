from .risk_reasoner import RiskReasoner
from .priority_engine import PriorityEngine
from .action_recommender import ActionRecommender
from .decision_model import DecisionModel


class DecisionOrchestrator:

    def __init__(self):
        self.risk_reasoner = RiskReasoner()
        self.priority_engine = PriorityEngine()
        self.action_recommender = ActionRecommender()


    def orchestrate(self, intelligence):

        risk = self.risk_reasoner.analyze(
            intelligence
        )

        priority = self.priority_engine.calculate(
            risk
        )

        actions = self.action_recommender.recommend(
            risk["risk_level"]
        )

        return DecisionModel(
            decision_type="security_response",
            confidence=0.85,
            priority=priority,
            actions=actions
        )