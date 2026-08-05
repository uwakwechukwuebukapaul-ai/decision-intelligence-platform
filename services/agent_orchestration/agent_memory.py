class AgentMemory:
    """
    Memory layer for autonomous agents.
    Stores investigation history,
    decisions and previous actions.
    """

    def __init__(self):

        self.memory = {}


    def remember(
        self,
        agent,
        data
    ):

        if agent not in self.memory:
            self.memory[agent] = []

        self.memory[agent].append(
            data
        )


    def recall(
        self,
        agent
    ):

        return self.memory.get(
            agent,
            []
        )


    def clear(
        self,
        agent
    ):

        if agent in self.memory:
            del self.memory[agent]