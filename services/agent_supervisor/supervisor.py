from .agent_health import AgentHealthMonitor
from .task_manager import AgentTaskManager
from .priority_engine import PriorityEngine
from .governance import AgentGovernance



class AgentSupervisor:
    """
    Central supervisor for autonomous agents.

    Responsibilities:

    - Monitor agents
    - Manage tasks
    - Prioritize execution
    - Enforce governance
    """

    def __init__(self):

        self.health = AgentHealthMonitor()

        self.tasks = AgentTaskManager()

        self.priority = PriorityEngine()

        self.governance = AgentGovernance()



    def register_agent(
        self,
        agent_name
    ):

        return self.health.register_agent(
            agent_name
        )


    def submit_task(
        self,
        agent,
        task,
        severity="medium",
        confidence=1
    ):

        priority = self.priority.calculate_priority(
            severity,
            confidence
        )


        return self.tasks.create_task(
            agent,
            task,
            priority
        )


    def supervise(self):

        return {

            "agents":
                self.health.all_agents(),

            "tasks":
                self.tasks.get_tasks(),

            "governance":
                self.governance.export()

        }