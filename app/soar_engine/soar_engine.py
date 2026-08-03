from datetime import datetime


from .playbook_manager import PlaybookManager
from .action_engine import ActionEngine
from .approval_manager import ApprovalManager
from .automation_executor import AutomationExecutor
from .workflow_orchestrator import WorkflowOrchestrator
from .integration_manager import IntegrationManager
from .soar_memory import SOARMemory



class SOAREngine:
    """
    Sentinel DNA Autonomous SOAR Engine.
    """


    def __init__(self):

        self.playbooks = PlaybookManager()

        self.actions = ActionEngine()

        self.approvals = ApprovalManager()

        self.executor = AutomationExecutor()

        self.workflow = WorkflowOrchestrator()

        self.integrations = IntegrationManager()

        self.memory = SOARMemory()



    def execute(
        self,
        incident
    ):


        playbook = self.playbooks.get_playbook(
            incident
        )


        actions = self.actions.generate(
            incident
        )


        approval = self.approvals.check(
            actions["actions"][0]
        )


        execution = self.executor.execute(
            actions["actions"][0]
        )


        workflow = self.workflow.orchestrate(
            incident
        )


        result = {

            "status":
                "completed",

            "incident":
                incident,

            "playbook":
                playbook,

            "actions":
                actions,

            "approval":
                approval,

            "execution":
                execution,

            "workflow":
                workflow,

            "integrations":
                self.integrations.available_services(),

            "created_at":
                datetime.utcnow().isoformat()

        }


        self.memory.store(
            result
        )


        return result