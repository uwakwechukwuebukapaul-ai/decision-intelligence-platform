class AgentLoader:
    """
    Dynamic autonomous agent loader.

    Connects agent implementations
    with the Agent Registry.
    """


    def __init__(
        self,
        registry
    ):

        self.registry = registry



    def register_agent(
        self,
        agent
    ):

        name = getattr(
            agent,
            "name",
            agent.__class__.__name__
        )


        self.registry.register(
            name,
            agent
        )


        return {
            "agent": name,
            "status": "registered"
        }



    def load_agents(
        self,
        agents
    ):

        results = {}


        for agent in agents:

            try:

                result = self.register_agent(
                    agent()
                )

                results[
                    result["agent"]
                ] = "loaded"


            except Exception as error:

                results[
                    str(agent)
                ] = f"failed: {error}"


        return results