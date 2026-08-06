"""
Sentinel DNA Agent Registry

Controls available AI investigation agents.
"""


class AgentRegistry:


    def __init__(self):

        self.agents = {}



    def register(
        self,
        agent
    ):

        self.agents[agent.name] = agent



    def get(
        self,
        name
    ):

        return self.agents.get(name)



    def list_agents(self):

        return list(
            self.agents.keys()
        )



    def run_agent(
        self,
        name,
        investigation
    ):

        agent = self.get(name)


        if not agent:

            raise ValueError(
                f"Agent {name} not found"
            )


        return agent.analyze(
            investigation
        )