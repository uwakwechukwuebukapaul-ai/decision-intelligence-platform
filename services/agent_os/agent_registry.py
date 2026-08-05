class AgentRegistry:
    """
    Sentinel DNA Agent Registry.

    Maintains autonomous AI agent inventory,
    capabilities and lifecycle state.
    """


    def __init__(self):

        self.agents = {}


    def register(
        self,
        name,
        agent_type,
        capabilities
    ):

        self.agents[name] = {

            "name": name,

            "type": agent_type,

            "capabilities": capabilities,

            "status": "active"

        }


        return self.agents[name]


    def get_agent(
        self,
        name
    ):

        return self.agents.get(
            name
        )


    def list_agents(
        self
    ):

        return list(
            self.agents.values()
        )


    def update_status(
        self,
        name,
        status
    ):

        if name in self.agents:

            self.agents[name]["status"] = status


        return self.agents.get(name)