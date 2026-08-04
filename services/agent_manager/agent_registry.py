class AgentRegistry:
    """
    Registry of available autonomous agents.
    """


    def __init__(self):

        self.agents = {}



    def register(
        self,
        name,
        agent
    ):

        self.agents[name] = agent

        return {

            "status": "registered",

            "agent": name

        }



    def get(
        self,
        name
    ):

        return self.agents.get(
            name
        )



    def list_agents(self):

        return list(
            self.agents.keys()
        )