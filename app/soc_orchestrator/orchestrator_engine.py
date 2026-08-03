from datetime import datetime

from .decision_engine import DecisionEngine
from .incident_router import IncidentRouter
from .investigation_planner import InvestigationPlanner
from .response_manager import ResponseManager
from .approval_controller import ApprovalController
from .workflow_engine import WorkflowEngine
from .orchestrator_memory import OrchestratorMemory


class SOCOrchestratorEngine:

    def __init__(self):
        self.decision = DecisionEngine()
        self.router = IncidentRouter()
        self.investigation = InvestigationPlanner()
        self.response = ResponseManager()
        self.approval = ApprovalController()
        self.workflow = WorkflowEngine()
        self.memory = OrchestratorMemory()

    def orchestrate(self, incident):

        decision = self.decision.evaluate(incident)

        route = self.router.route(incident)

        investigation = self.investigation.plan(incident)

        approval = self.approval.check(
            decision["priority"]
        )

        response = self.response.prepare(
            incident
        )

        workflow = self.workflow.execute(
            incident
        )

        self.memory.store(incident)

        return {
            "status": "completed",
            "incident": incident,
            "decision": decision,
            "routing": route,
            "investigation": investigation,
            "approval": approval,
            "response": response,
            "workflow": workflow,
            "created_at": datetime.now().isoformat()
        }