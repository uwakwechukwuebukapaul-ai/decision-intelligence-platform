from datetime import datetime

from .playbook_engine import PlaybookEngine
from .action_executor import ActionExecutor
from .response_orchestrator import ResponseOrchestrator
from .workflow_manager import WorkflowManager
from .integration_manager import IntegrationManager
from .approval_engine import ApprovalEngine
from .soar_memory import SOARMemory
from .soar_logger import SOARLogger


class SOAREngine:


    def __init__(self):

        self.playbooks = PlaybookEngine()
        self.actions = ActionExecutor()
        self.response = ResponseOrchestrator()
        self.workflow = WorkflowManager()
        self.integrations = IntegrationManager()
        self.approval = ApprovalEngine()
        self.memory = SOARMemory()
        self.logger = SOARLogger()


    def execute(self, incident):

        playbook = self.playbooks.generate(
            incident
        )

        action = self.actions.execute(
            "Isolate affected endpoint"
        )

        response = self.response.orchestrate(
            incident
        )

        workflow = self.workflow.manage(
            incident
        )

        integrations = self.integrations.connect(
            incident
        )

        approval = self.approval.approve(
            "Containment Action"
        )

        memory = self.memory.store(
            incident
        )

        log = self.logger.log(
            incident
        )


        return {

            "status": "completed",

            "incident": incident,

            "playbook": playbook,

            "action_execution": action,

            "response": response,

            "workflow": workflow,

            "integrations": integrations,

            "approval": approval,

            "memory": memory,

            "log": log,

            "created_at":
                datetime.utcnow().isoformat()
        }