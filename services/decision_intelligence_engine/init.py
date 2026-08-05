from .decision_engine import DecisionEngine
from .decision_model import DecisionModel
from .risk_reasoner import RiskReasoner
from .priority_engine import PriorityEngine
from .action_recommender import ActionRecommender
from .analyst_advisor import AnalystAdvisor
from .decision_orchestrator import DecisionOrchestrator


class DecisionIntelligenceEngine:

    def __init__(self):
        self.engine = DecisionEngine()
        self.model = DecisionModel()
        self.risk = RiskReasoner()
        self.priority = PriorityEngine()
        self.actions = ActionRecommender()
        self.advisor = AnalystAdvisor()
        self.orchestrator = DecisionOrchestrator()


    def analyze(self, incident):

        return self.orchestrator.process(
            incident
        )