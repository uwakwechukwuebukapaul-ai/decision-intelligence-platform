class AgentHealthMonitor:
    """
    Monitors autonomous agent health state.
    """

    def __init__(self):
        self.agents = {}

    def register_agent(self, agent_name):

        self.agents[agent_name] = {
            "status": "active",
            "tasks_completed": 0,
            "errors": 0
        }

        return self.agents[agent_name]


    def update_health(
        self,
        agent_name,
        status=None,
        error=False
    ):

        if agent_name not in self.agents:
            self.register_agent(agent_name)

        if status:
            self.agents[agent_name]["status"] = status

        if error:
            self.agents[agent_name]["errors"] += 1

        return self.agents[agent_name]


    def get_health(self, agent_name):

        return self.agents.get(agent_name)


    def all_agents(self):

        return self.agents