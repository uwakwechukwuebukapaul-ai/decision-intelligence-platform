from .response_engine import ResponseEngine
from .containment_engine import ContainmentEngine
from .remediation_engine import RemediationEngine
from .decision_engine import ResponseDecisionEngine
from .response_planner import ResponsePlanner
from .risk_controller import RiskController
from .response_orchestrator import ResponseOrchestrator


class IncidentResponseIntelligence:

    def __init__(self):
        self.response = ResponseEngine()
        self.containment = ContainmentEngine()
        self.remediation = RemediationEngine()
        self.decision = ResponseDecisionEngine()
        self.planner = ResponsePlanner()
        self.risk = RiskController()
        self.orchestrator = ResponseOrchestrator()

    def status(self):
        return {
            "module": "incident_response_intelligence",
            "status": "ready"
        }