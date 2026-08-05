from .threat_understanding_engine import ThreatUnderstandingEngine
from .behavior_analysis_engine import BehaviorAnalysisEngine
from .security_reasoning_engine import SecurityReasoningEngine
from .autonomous_learning_engine import AutonomousLearningEngine
from .knowledge_synthesis_engine import KnowledgeSynthesisEngine
from .intelligence_memory_manager import IntelligenceMemoryManager


class SecurityIntelligenceOS:

    def __init__(self):
        self.threat_engine = ThreatUnderstandingEngine()
        self.behavior_engine = BehaviorAnalysisEngine()
        self.reasoning_engine = SecurityReasoningEngine()
        self.learning_engine = AutonomousLearningEngine()
        self.synthesis_engine = KnowledgeSynthesisEngine()
        self.memory_manager = IntelligenceMemoryManager()

    def analyze(self, intelligence):

        threat = self.threat_engine.analyze(intelligence)

        behavior = self.behavior_engine.analyze(
            intelligence
        )

        reasoning = self.reasoning_engine.reason(
            threat,
            behavior
        )

        self.memory_manager.store(
            {
                "input": intelligence,
                "reasoning": reasoning
            }
        )

        return {
            "threat": threat,
            "behavior": behavior,
            "reasoning": reasoning
        }