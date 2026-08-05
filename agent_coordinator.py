class AgentCoordinator:

    def __init__(self):
        self.agents = []

    def register_agent(self, agent_name):
        self.agents.append(agent_name)

        return {
            "agent": agent_name,
            "registered": True
        }


    def list_agents(self):
        return self.agents