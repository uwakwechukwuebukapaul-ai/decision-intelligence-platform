from datetime import datetime

from .playbook_manager import PlaybookManager
from .action_executor import ActionExecutor
from .automation_router import AutomationRouter
from .containment_actions import ContainmentActions
from .integration_manager import IntegrationManager
from .workflow_memory import WorkflowMemory
from .workflow_logger import WorkflowLogger


class SOAREngine:

    def __init__(self):
        self.playbooks = PlaybookManager()
        self.executor = ActionExecutor()
        self.router = AutomationRouter()
        self.containment = ContainmentActions()
        self.integrations = IntegrationManager()
        self.memory = WorkflowMemory()
        self.logger = WorkflowLogger()

    def execute(self, incident):

        playbook = self.playbooks.select(incident)

        routing = self.router.route(
            incident
        )

        actions = self.containment.execute(
            incident
        )

        execution = self.executor.execute(
            actions
        )

        integrations = self.integrations.connect(
            incident
        )

        memory = self.memory.store(
            incident
        )

        log = self.logger.record(
            incident
        )

        return {
            "status": "completed",
            "incident": incident,
            "playbook": playbook,
            "routing": routing,
            "actions": actions,
            "execution": execution,
            "integrations": integrations,
            "memory": memory,
            "log": log,
            "created_at": datetime.utcnow().isoformat()
        }