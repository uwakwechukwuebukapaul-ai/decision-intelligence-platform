class AgentRegistry:
    """
    Registry for managing autonomous SOC agents.
    """

    def __init__(self):

        self.agents = {}


    def register(
        self,
        name,
        agent
    ):

        self.agents[name] = agent


    def unregister(
        self,
        name
    ):

        if name in self.agents:
            del self.agents[name]


    def get(
        self,
        name
    ):

        return self.agents.get(name)


    def list_agents(self):

        return list(
            self.agents.keys()
        )


    def exists(
        self,
        name
    ):

        return name in self.agents