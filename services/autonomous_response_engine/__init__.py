from .response_engine import ResponseEngine
from .playbook_manager import PlaybookManager
from .action_executor import ActionExecutor
from .remediation_engine import RemediationEngine
from .automation_policy import AutomationPolicy
from .approval_manager import ApprovalManager
from .response_memory import ResponseMemory
from .response_orchestrator import ResponseOrchestrator


class AutonomousResponseEngine:
    """
    Sentinel DNA Autonomous Response & SOAR Engine.

    Capabilities:
    - automated response planning
    - SOAR playbook execution
    - remediation workflows
    - approval governance
    - response learning memory
    """

    def __init__(self):

        self.response_engine = ResponseEngine()
        self.playbooks = PlaybookManager()
        self.executor = ActionExecutor()
        self.remediation = RemediationEngine()
        self.policy = AutomationPolicy()
        self.approvals = ApprovalManager()
        self.memory = ResponseMemory()
        self.orchestrator = ResponseOrchestrator()


    def status(self):

        return {
            "engine": "Autonomous Response Engine",
            "status": "operational"
        }