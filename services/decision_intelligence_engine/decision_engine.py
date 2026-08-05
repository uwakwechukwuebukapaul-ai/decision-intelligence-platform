from .decision_orchestrator import DecisionOrchestrator


class DecisionIntelligenceEngine:

    def __init__(self):

        self.orchestrator = DecisionOrchestrator()


    def evaluate(self, intelligence):

        decision = self.orchestrator.orchestrate(
            intelligence
        )

        return decision.to_dict()