class AgentSupervisor:

    def __init__(self):
        self.status = {}

    def monitor(self, agent_name):

        self.status[agent_name] = "healthy"

        return {
            "agent": agent_name,
            "status": "healthy"
        }

    def get_status(self):

        return self.status