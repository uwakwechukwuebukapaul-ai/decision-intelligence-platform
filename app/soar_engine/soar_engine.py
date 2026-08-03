from datetime import datetime

from .playbook_manager import PlaybookManager
from .automation_engine import AutomationEngine
from .action_executor import ActionExecutor
from .integration_manager import IntegrationManager
from .approval_manager import ApprovalManager
from .workflow_orchestrator import WorkflowOrchestrator
from .soar_memory import SOARMemory
from .soar_logger import SOARLogger


class SOAREngine:

    def __init__(self):
        self.playbooks = PlaybookManager()
        self.automation = AutomationEngine()
        self.executor = ActionExecutor()
        self.integrations = IntegrationManager()
        self.approvals = ApprovalManager()
        self.workflow = WorkflowOrchestrator()
        self.memory = SOARMemory()
        self.logger = SOARLogger()

    def execute(self, incident):

        playbook = self.playbooks.select(incident)

        automation = self.automation.analyze(incident)

        actions = self.executor.prepare(
            automation
        )

        integrations = self.integrations.connect()

        approval = self.approvals.check(
            actions
        )

        workflow = self.workflow.create(
            incident,
            actions
        )

        memory = self.memory.store(
            incident,
            actions
        )

        log = self.logger.log(
            incident
        )

        return {
            "status": "completed",
            "incident": incident,
            "playbook": playbook,
            "automation": automation,
            "actions": actions,
            "integrations": integrations,
            "approval": approval,
            "workflow": workflow,
            "memory": memory,
            "log": log,
            "created_at": datetime.utcnow().isoformat()
        }