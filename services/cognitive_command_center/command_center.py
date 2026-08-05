from .investigation_controller import InvestigationController
from .decision_orchestrator import DecisionOrchestrator
from .analyst_copilot import AnalystCopilot
from .executive_summary import ExecutiveSummary


class CognitiveCommandCenter:
    """
    Central cognitive coordination layer.

    Responsible for:
    - investigation coordination
    - analyst assistance
    - decision orchestration
    - executive reporting
    """

    def __init__(self):

        self.investigation_controller = InvestigationController()

        self.decision_orchestrator = DecisionOrchestrator()

        self.analyst_copilot = AnalystCopilot()

        self.executive_summary = ExecutiveSummary()


    def analyze(self, case):

        investigation = self.investigation_controller.run(
            case
        )

        decision = self.decision_orchestrator.evaluate(
            investigation
        )

        copilot = self.analyst_copilot.assist(
            investigation
        )

        summary = self.executive_summary.generate(
            investigation,
            decision
        )


        return {

            "investigation":
            investigation,

            "decision":
            decision,

            "copilot":
            copilot,

            "summary":
            summary
        }


    def status(self):

        return {

            "service":
            "Cognitive Command Center",

            "status":
            "operational"
        }