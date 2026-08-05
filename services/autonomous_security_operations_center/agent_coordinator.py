class AgentCoordinator:
    """
    Coordinates AI agents operating inside Sentinel DNA SOC.

    Responsibilities:
    - register agents
    - assign tasks
    - track execution state
    - coordinate multi-agent workflows
    """

    def __init__(self):
        self.agents = {}
        self.tasks = []


    def register_agent(self, agent_name, agent):

        self.agents[agent_name] = agent

        return {
            "agent": agent_name,
            "status": "registered"
        }


    def assign_task(self, agent_name, task):

        assignment = {
            "agent": agent_name,
            "task": task,
            "status": "assigned"
        }

        self.tasks.append(assignment)

        return assignment


    def execute_task(self, agent_name, task):

        result = {
            "agent": agent_name,
            "task": task,
            "result": "completed"
        }

        return result


    def list_agents(self):

        return list(self.agents.keys())


    def health(self):

        return {
            "component": "AgentCoordinator",
            "agents": len(self.agents),
            "tasks": len(self.tasks),
            "status": "healthy"
        }