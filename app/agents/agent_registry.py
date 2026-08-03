class AgentRegistry:


    def __init__(self):

        self.agents = {
            "SOC Agent": "Security investigation agent",
            "Research Agent": "Threat intelligence research agent",
            "Threat Hunting Agent": "Adversary hunting agent",
            "Compliance Agent": "Security compliance agent",
            "Executive Agent": "Business intelligence agent"
        }


    def list_agents(self):

        return {
            "available_agents": self.agents
        }


    def get_agent(self,name):

        return self.agents.get(
            name,
            "Agent unavailable"
        )