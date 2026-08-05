from .investigation_controller import InvestigationController
from .decision_orchestrator import DecisionOrchestrator
from .analyst_copilot import AnalystCopilot
from .executive_summary import ExecutiveSummary


class CognitiveCommandCenter:
    """
    Central AI SOC operational command layer.
    """

    def __init__(self):

        self.investigation = InvestigationController()
        self.decision = DecisionOrchestrator()
        self.copilot = AnalystCopilot()
        self.summary = ExecutiveSummary()


    def process_alert(self, alert):

        investigation = self.investigation.start(
            alert
        )

        decision = self.decision.evaluate(
            investigation
        )

        assistance = self.copilot.generate(
            investigation,
            decision
        )

        report = self.summary.create(
            investigation,
            decision
        )


        return {

            "investigation": investigation,

            "decision": decision,

            "copilot": assistance,

            "executive_summary": report
        }