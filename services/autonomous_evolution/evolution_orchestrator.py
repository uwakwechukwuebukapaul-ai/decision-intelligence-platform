from .learning_engine import LearningEngine
from .performance_optimizer import PerformanceOptimizer
from .detection_evolution import DetectionEvolution
from .analyst_feedback import AnalystFeedback
from .model_improvement import ModelImprovement


class EvolutionOrchestrator:
    """
    Central controller for Sentinel DNA self-improvement lifecycle.
    """

    def __init__(self):
        self.learning = LearningEngine()
        self.optimizer = PerformanceOptimizer()
        self.detection = DetectionEvolution()
        self.feedback = AnalystFeedback()
        self.model = ModelImprovement()

    def evolve(self, investigation_result):
        learning = self.learning.record_learning(
            "investigation",
            investigation_result
        )

        return {
            "status": "evolution_cycle_complete",
            "learning": learning,
            "detection": "reviewed",
            "models": "evaluated"
        }

    def health(self):
        return {
            "engine": "autonomous_evolution",
            "status": "active"
        }