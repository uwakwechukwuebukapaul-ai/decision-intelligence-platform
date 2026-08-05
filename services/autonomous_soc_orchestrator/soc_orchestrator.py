from .workflow_engine import WorkflowEngine
from .decision_router import DecisionRouter
from .intelligence_router import IntelligenceRouter
from .investigation_controller import InvestigationController
from .automation_controller import AutomationController
from .orchestration_runtime import OrchestrationRuntime


class AutonomousSOCOrchestrator:

    def __init__(self):

        self.workflow_engine = WorkflowEngine()
        self.decision_router = DecisionRouter()
        self.intelligence_router = IntelligenceRouter()
        self.investigation_controller = InvestigationController()
        self.automation_controller = AutomationController()
        self.runtime = OrchestrationRuntime()


    def process_event(self, event):

        investigation_id = self.runtime.create_execution(event)

        intelligence = self.intelligence_router.collect(event)

        investigation = self.investigation_controller.start(
            event,
            intelligence
        )

        decision = self.decision_router.evaluate(
            event,
            investigation
        )

        response = self.automation_controller.execute(
            decision
        )

        self.runtime.complete_execution(
            investigation_id,
            response
        )

        return {
            "execution_id": investigation_id,
            "intelligence": intelligence,
            "investigation": investigation,
            "decision": decision,
            "response": response
        }