class AgentManager:
    """
    Manages lifecycle of AI SOC agents.
    """

    def __init__(self):
        self.agents = {}

    def create_agent(self, name, agent):
        self.agents[name] = agent

        return {
            "name": name,
            "status": "created"
        }

    def get_agent(self, name):
        return self.agents.get(name)

    def remove_agent(self, name):
        if name in self.agents:
            del self.agents[name]

        return {
            "name": name,
            "status": "removed"
        }

    def list_agents(self):
        return list(self.agents.keys())