from services.autonomous_security_operations_center.soc_runtime import SOCRuntime
from .event_processor import EventProcessor
from .investigation_pipeline import InvestigationPipeline
from .decision_pipeline import DecisionPipeline
from .response_pipeline import ResponsePipeline
from .workflow_manager import WorkflowManager
from .execution_controller import ExecutionController
from .runtime_orchestrator import RuntimeOrchestrator


class AutonomousSOCRuntime:
    """
    Sentinel DNA Autonomous SOC Runtime.

    Central execution layer connecting:
    - Threat Intelligence
    - Investigation
    - Decision Intelligence
    - Response Automation
    - Analyst Experience
    """

    def __init__(self):

        self.runtime = SOCRuntime()
        self.events = EventProcessor()
        self.investigation = InvestigationPipeline()
        self.decision = DecisionPipeline()
        self.response = ResponsePipeline()
        self.workflow = WorkflowManager()
        self.execution = ExecutionController()
        self.orchestrator = RuntimeOrchestrator()


    def status(self):

        return {
            "component": "Autonomous SOC Runtime",
            "status": "operational"
        }