class AgentMemory:
    """
    Stores autonomous agent experiences.
    """

    def __init__(self):

        self.history = []


    def remember(
        self,
        task,
        result
    ):

        self.history.append(
            {
                "task": task,
                "result": result
            }
        )


        return {

            "memory_status":
                "stored",

            "entries":
                len(self.history)

        }


    def recall(self):

        return self.history