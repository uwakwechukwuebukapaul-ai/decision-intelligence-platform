from .response_engine import ResponseEngine
from .containment_engine import ContainmentEngine
from .remediation_engine import RemediationEngine
from .decision_engine import DecisionEngine
from .response_planner import ResponsePlanner
from .risk_controller import RiskController
from .response_orchestrator import ResponseOrchestrator


class IncidentResponseIntelligence:

    def __init__(self):

        self.response_engine = ResponseEngine()
        self.containment_engine = ContainmentEngine()
        self.remediation_engine = RemediationEngine()
        self.decision_engine = DecisionEngine()
        self.response_planner = ResponsePlanner()
        self.risk_controller = RiskController()
        self.orchestrator = ResponseOrchestrator()


    def status(self):

        return {
            "module": "Incident Response Intelligence",
            "status": "ready"
        }