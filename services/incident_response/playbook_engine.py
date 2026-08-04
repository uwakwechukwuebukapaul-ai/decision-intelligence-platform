from .response_executor import ResponseExecutor
from .containment_engine import ContainmentEngine
from .remediation_engine import RemediationEngine
from .automation_rules import AutomationRules
from .response_logger import ResponseLogger


class IncidentResponseEngine:

    def __init__(self):

        self.executor = ResponseExecutor()
        self.containment = ContainmentEngine()
        self.remediation = RemediationEngine()
        self.rules = AutomationRules()
        self.logger = ResponseLogger()


    def respond(self, incident):

        actions = self.rules.evaluate(incident)

        containment = self.containment.execute(
            actions
        )

        remediation = self.remediation.execute(
            actions
        )

        execution = self.executor.run(
            actions
        )

        result = {
            "incident": incident,
            "actions": actions,
            "containment": containment,
            "remediation": remediation,
            "execution": execution,
            "status": "incident_response_completed"
        }

        self.logger.log(result)

        return result