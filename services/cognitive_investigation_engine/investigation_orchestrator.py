from .investigation_engine import CognitiveInvestigationEngine
from .investigation_memory import InvestigationMemory
from .analyst_reasoning_engine import AnalystReasoningEngine


class InvestigationOrchestrator:


    def __init__(self):

        self.engine = CognitiveInvestigationEngine()

        self.memory = InvestigationMemory()

        self.reasoner = AnalystReasoningEngine()


    def execute(self, case):

        investigation = self.engine.investigate(
            case
        )

        self.memory.store(
            investigation
        )

        reasoning = self.reasoner.reason(
            investigation
        )

        return {
            "investigation": investigation,
            "reasoning": reasoning
        }