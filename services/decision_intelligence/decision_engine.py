from .strategy_selector import StrategySelector
from .prediction_engine import PredictionEngine
from .confidence_model import ConfidenceModel
from .action_optimizer import ActionOptimizer
from .learning_feedback import LearningFeedback


class DecisionIntelligence:

    def __init__(self):
        self.strategy_selector = StrategySelector()
        self.prediction_engine = PredictionEngine()
        self.confidence_model = ConfidenceModel()
        self.action_optimizer = ActionOptimizer()
        self.learning_feedback = LearningFeedback()


    def analyze(self, context):

        prediction = self.prediction_engine.predict(context)

        confidence = self.confidence_model.calculate(
            prediction
        )

        strategy = self.strategy_selector.select(
            prediction,
            confidence
        )

        action = self.action_optimizer.optimize(
            strategy
        )

        return {
            "prediction": prediction,
            "confidence": confidence,
            "strategy": strategy,
            "action": action
        }


    def learn(self, feedback):

        return self.learning_feedback.process(
            feedback
        )