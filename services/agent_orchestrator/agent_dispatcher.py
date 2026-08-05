class AgentDispatcher:
    """
    Sends tasks to autonomous agents.
    """

    def dispatch(
        self,
        agent,
        task
    ):

        if hasattr(
            agent,
            "investigate"
        ):

            return agent.investigate(
                task.objective
            )


        return {

            "status":
                "agent_not_supported",

            "task":
                task.to_dict()

        }