class CognitiveMemory:
    """
    Cognitive memory bridge.

    Connects reasoning,
    learning and previous knowledge.
    """


    def __init__(self):

        self.memory = []



    def store(
        self,
        thought
    ):

        record = {

            "thought":
                thought,

            "type":
                "cognitive_memory"

        }


        self.memory.append(
            record
        )


        return record



    def recall(
        self
    ):

        return self.memory