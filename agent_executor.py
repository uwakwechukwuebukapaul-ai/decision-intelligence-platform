class AgentExecutor:

    def execute(self, agent, task):

        if hasattr(agent, "run"):
            return agent.run(task)

        return {
            "status": "failed",
            "reason": "Agent has no execution method"
        }