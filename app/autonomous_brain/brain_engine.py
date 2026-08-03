from datetime import datetime

from .perception_layer import PerceptionLayer
from .reasoning_layer import ReasoningLayer
from .action_layer import ActionLayer
from .learning_layer import LearningLayer
from .memory_layer import MemoryLayer
from .self_evaluation import SelfEvaluation
from .brain_orchestrator import BrainOrchestrator



class BrainEngine:
    """
    Sentinel DNA Autonomous Security Brain.

    Main intelligence controller.
    """


    def __init__(self):

        self.perception = PerceptionLayer()

        self.reasoning = ReasoningLayer()

        self.action = ActionLayer()

        self.learning = LearningLayer()

        self.memory = MemoryLayer()

        self.evaluation = SelfEvaluation()

        self.orchestrator = BrainOrchestrator()



    def analyze(self, security_event):


        perception_result = (
            self.perception.perceive(
                security_event
            )
        )


        reasoning_result = (
            self.reasoning.reason(
                perception_result
            )
        )


        action_result = (
            self.action.execute(
                reasoning_result
            )
        )


        learning_result = (
            self.learning.learn(
                security_event
            )
        )


        combined = {

            "reasoning":
                reasoning_result

        }


        evaluation_result = (
            self.evaluation.evaluate(
                combined
            )
        )


        result = self.orchestrator.run(

            perception_result,

            reasoning_result,

            action_result,

            learning_result,

            evaluation_result
        )


        self.memory.remember(result)


        return {

            "status":
                "completed",

            "event":
                security_event,

            "brain_output":
                result,

            "created_at":
                datetime.utcnow().isoformat()
        }