"""
Sentinel DNA

Agent Registry

Central registry for intelligence agents.
"""


class AgentRegistry:

    def __init__(self):

        self.agents = {}


    def register(
        self,
        agent,
    ):

        name = agent.metadata.name

        self.agents[name] = agent

        return name


    def unregister(
        self,
        name: str,
    ):

        if name in self.agents:

            del self.agents[name]


    def get(
        self,
        name: str,
    ):

        return self.agents.get(name)


    def get_by_capability(
        self,
        capability: str,
    ):

        """
        Find agent capable of executing a task.
        """

        for agent in self.agents.values():

            if capability in agent.capabilities:

                return agent


        return None


    def list_agents(self):

        return list(
            self.agents.keys()
        )


    def all_metadata(self):

        return [

            agent.get_metadata()

            for agent in self.agents.values()

        ]