class AgentExecutor:
    """
    Executes agent tasks.
    """

    def execute(self, agent, task):

        if hasattr(agent, "execute"):
            return agent.execute(task)

        return {
            "status": "completed",
            "task": task
        }