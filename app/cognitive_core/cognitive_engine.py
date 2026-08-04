import datetime

from .investigation_brain import InvestigationBrain
from .reasoning_engine import ReasoningEngine
from .confidence_manager import ConfidenceManager
from .decision_engine import DecisionEngine
from .recommendation_engine import RecommendationEngine
from .cognitive_memory import CognitiveMemory
from .cognitive_logger import CognitiveLogger


class CognitiveSecurityEngine:
    """
    Sentinel DNA Cognitive Security Engine

    Central reasoning layer that transforms
    security events into intelligence decisions.
    """

    def __init__(self):

        self.brain = InvestigationBrain()
        self.reasoner = ReasoningEngine()
        self.confidence = ConfidenceManager()
        self.decision = DecisionEngine()
        self.recommendation = RecommendationEngine()

        self.memory = CognitiveMemory()
        self.logger = CognitiveLogger()


    def investigate(self, event):

        context = self.brain.build_context(event)

        reasoning = self.reasoner.analyze(
            context
        )

        confidence = self.confidence.evaluate(
            reasoning
        )

        decision = self.decision.decide(
            reasoning,
            confidence
        )

        recommendations = self.recommendation.recommend(
            decision
        )


        memory = self.memory.store(
            {
                "event": event,
                "context": context,
                "reasoning": reasoning,
                "decision": decision
            }
        )


        log = self.logger.log(
            event
        )


        return {

            "status": "completed",

            "event": event,

            "context": context,

            "reasoning": reasoning,

            "confidence": confidence,

            "decision": decision,

            "recommendations": recommendations,

            "memory": memory,

            "log": log,

            "created_at":
                datetime.datetime.utcnow().isoformat()

        }