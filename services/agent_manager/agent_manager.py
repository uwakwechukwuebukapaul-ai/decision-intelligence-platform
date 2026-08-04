class AgentManager:
    """
    Coordinates autonomous SOC agents.
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

            "status":
                "registered",

            "agent":
                name

        }



    def execute(
        self,
        agent_name,
        event,
        context=None
    ):

        agent = self.agents.get(
            agent_name
        )


        if not agent:

            return {

                "error":
                    f"Agent {agent_name} unavailable"

            }



        return agent.execute(
            event,
            context or {}
        )



    def execute_all(
        self,
        event,
        context=None
    ):

        results = {}


        for name in self.agents:

            results[name] = self.execute(

                name,

                event,

                context

            )


        return results



    def list_agents(self):

        return list(
            self.agents.keys()
        )