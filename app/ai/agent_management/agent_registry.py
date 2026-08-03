class AgentRegistry:
    """
    Maintains registered autonomous agents.
    """

    def __init__(self):
        self.agents = {}


    def register_agent(self, agent_id, metadata=None):

        self.agents[agent_id] = {

            "agent_id": agent_id,

            "metadata": metadata or {},

            "status": "active"

        }

        return self.agents[agent_id]


    def get_agents(self):

        return list(self.agents.values())


    def get_agent(self, agent_id):

        return self.agents.get(agent_id)