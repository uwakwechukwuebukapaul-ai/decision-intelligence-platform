from .memory_context import MemoryContext
from .pattern_engine import PatternEngine
from .learning_engine import LearningEngine


class MemoryController:
    """
    Central cognitive memory API.

    Handles:
    - Remember
    - Retrieve
    - Learn
    """

    def __init__(self):

        self.pattern_engine = PatternEngine()

        self.learning_engine = LearningEngine()

        self.storage = []


    def remember(
        self,
        investigation_id,
        event,
        decision,
        outcome
    ):

        memory = MemoryContext(

            investigation_id,

            event,

            decision,

            outcome
        )


        patterns = self.pattern_engine.analyze(
            event
        )


        for pattern in patterns:

            memory.add_pattern(
                pattern
            )


        self.storage.append(
            memory
        )


        return memory.snapshot()



    def retrieve(
        self
    ):

        return [

            item.snapshot()

            for item in self.storage

        ]



    def learn(
        self
    ):

        results = []


        for memory in self.storage:

            results.append(

                self.learning_engine.learn(
                    memory
                )

            )


        return results