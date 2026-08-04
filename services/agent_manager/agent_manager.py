from .agent_registry import AgentRegistry
from .task_router import TaskRouter



class AgentManager:
    """
    Autonomous SOC agent coordinator.

    Responsible for:
    - agent registration
    - task routing
    - execution delegation
    """


    def __init__(self):

        self.registry = AgentRegistry()

        self.router = TaskRouter()



    def register_agent(
        self,
        name,
        agent
    ):

        return self.registry.register(
            name,
            agent
        )



    def execute_task(
        self,
        task
    ):

        agent_name = self.router.route(
            task
        )


        agent = self.registry.get(
            agent_name
        )


        if not agent:

            return {

                "status":
                    "agent_unavailable",

                "agent":
                    agent_name

            }



        result = agent.execute(
            task
        )


        return {

            "status":
                "completed",

            "agent":
                agent_name,

            "result":
                result

        }



    def available_agents(self):

        return {

            "agents":
                self.registry.list_agents()

        }