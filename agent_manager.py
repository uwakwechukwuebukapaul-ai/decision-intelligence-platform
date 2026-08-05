class AgentManager:

    def __init__(self, registry):

        self.registry = registry


    def create_agent(self, name, agent):

        return self.registry.register_agent(
            name,
            agent
        )


    def get_agents(self):

        return self.registry.list_agents()