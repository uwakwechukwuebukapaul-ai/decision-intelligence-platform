class AgentRegistry:

    def __init__(self):
        self.agents = {}

    def register_agent(self, name, agent):
        self.agents[name] = agent
        return True

    def get_agent(self, name):
        return self.agents.get(name)

    def list_agents(self):
        return list(self.agents.keys())

    def remove_agent(self, name):
        if name in self.agents:
            del self.agents[name]
            return True

        return False