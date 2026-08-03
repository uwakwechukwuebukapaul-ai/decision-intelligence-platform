from datetime import datetime

from .reasoning_engine import ReasoningEngine
from .context_builder import ContextBuilder
from .recommendation_engine import RecommendationEngine
from .action_selector import ActionSelector
from .decision_memory import DecisionMemory
from .confidence_engine import ConfidenceEngine
from .decision_logger import DecisionLogger


class DecisionEngine:

    def __init__(self):

        self.reasoning = ReasoningEngine()
        self.context = ContextBuilder()
        self.recommendation = RecommendationEngine()
        self.actions = ActionSelector()
        self.memory = DecisionMemory()
        self.confidence = ConfidenceEngine()
        self.logger = DecisionLogger()


    def decide(self, incident):

        context = self.context.build(incident)

        reasoning = self.reasoning.analyze(
            incident,
            context
        )

        recommendations = self.recommendation.generate(
            incident,
            reasoning
        )

        actions = self.actions.select(
            incident,
            recommendations
        )

        confidence = self.confidence.calculate(
            reasoning
        )

        memory = self.memory.store(
            incident,
            reasoning
        )

        log = self.logger.record(
            incident,
            actions
        )


        return {

            "status": "completed",

            "incident": incident,

            "context": context,

            "reasoning": reasoning,

            "recommendations": recommendations,

            "actions": actions,

            "confidence": confidence,

            "memory": memory,

            "log": log,

            "created_at": datetime.utcnow().isoformat()

        }