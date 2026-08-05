from .playbook_engine import PlaybookEngine
from .action_executor import ActionExecutor
from .response_actions import ResponseActions
from .automation_rules import AutomationRules
from .approval_engine import ApprovalEngine
from .workflow_manager import WorkflowManager


class SOARAutomation:
    """
    Sentinel DNA SOAR Automation Engine.

    Responsible for:
    - security playbook execution
    - automated response actions
    - workflow orchestration
    - approval governance
    """

    def __init__(self):
        self.playbooks = PlaybookEngine()
        self.executor = ActionExecutor()
        self.actions = ResponseActions()
        self.rules = AutomationRules()
        self.approvals = ApprovalEngine()
        self.workflow = WorkflowManager()

    def execute(self, incident):

        workflow = self.workflow.create(incident)

        return {
            "status": "executed",
            "workflow": workflow,
            "actions": self.actions.available()
        }


__all__ = [
    "SOARAutomation",
    "PlaybookEngine",
    "ActionExecutor",
    "ResponseActions",
    "AutomationRules",
    "ApprovalEngine",
    "WorkflowManager",
]