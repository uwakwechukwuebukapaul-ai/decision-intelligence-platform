class AgentExecutor:
    """
    Executes registered autonomous agents.
    """

    def execute(
        self,
        agent,
        task
    ):

        if hasattr(
            agent,
            "run"
        ):

            return agent.run(
                task
            )


        if callable(agent):

            return agent(
                task
            )


        return {

            "status": "failed",

            "reason":
            "Agent cannot execute tasks"

        }