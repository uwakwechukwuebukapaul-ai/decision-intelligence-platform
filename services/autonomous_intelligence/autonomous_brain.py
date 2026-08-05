from .intelligence_orchestrator import IntelligenceOrchestrator
from .decision_cycle import DecisionCycle
from .self_reasoning import SelfReasoning
from .adaptive_response import AdaptiveResponse


class AutonomousBrain:
    """
    Sentinel DNA Autonomous Intelligence Brain

    Central reasoning controller that coordinates:

    - Intelligence collection
    - Decision cycles
    - Self reasoning
    - Adaptive improvement
    """

    def __init__(self):

        self.orchestrator = IntelligenceOrchestrator()

        self.decision_cycle = DecisionCycle()

        self.reasoning = SelfReasoning()

        self.adaptation = AdaptiveResponse()


    def analyze(self, event):

        intelligence = self.orchestrator.collect(
            event
        )


        decision = self.decision_cycle.execute(
            event,
            intelligence
        )


        reasoning = self.reasoning.evaluate(
            event,
            intelligence,
            decision
        )


        adaptation = self.adaptation.optimize(
            decision
        )


        return {

            "status": "autonomous_completed",

            "event": event,

            "intelligence": intelligence,

            "decision": decision,

            "reasoning": reasoning,

            "adaptation": adaptation

        }