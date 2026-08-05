class AIAgentRuntime:
    """
    Core execution runtime for Sentinel DNA AI agents.
    """

    def __init__(self):
        self.agents = {}
        self.status = "initialized"

    def register_agent(self, name, agent):
        self.agents[name] = agent
        return {
            "agent": name,
            "status": "registered"
        }

    def execute(self, agent_name, task):
        agent = self.agents.get(agent_name)

        if not agent:
            return {
                "status": "failed",
                "reason": "agent_not_found"
            }

        return agent.execute(task)

    def health(self):
        return {
            "runtime": "AI Agent Runtime",
            "status": "healthy",
            "agents": len(self.agents)
        }