from .decision_context import DecisionContext
from .reasoning_controller import ReasoningController
from .decision_executor import DecisionExecutor


class AutonomousLoop:
    """
    Sentinel DNA autonomous reasoning cycle.

    Observe
    Understand
    Decide
    Act
    """

    def __init__(self):

        self.reasoner = ReasoningController()

        self.executor = DecisionExecutor()


    def run(
        self,
        event,
        intelligence=None,
        evidence=None,
        memory=None
    ):

        context = DecisionContext(

            event=event,

            intelligence=intelligence,

            evidence=evidence,

            memory=memory
        )


        reasoning = self.reasoner.reason(
            context
        )


        decision = self.executor.execute(
            reasoning
        )


        context.update_decision(
            decision
        )


        return context.snapshot()