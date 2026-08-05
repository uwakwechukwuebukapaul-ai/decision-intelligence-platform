from .agent_registry import AgentRegistry
from .agent_dispatcher import AgentDispatcher



class AgentOrchestrator:
    """
    Sentinel DNA Multi-Agent Coordinator.

    Manages autonomous security agents.
    """

    def __init__(self):

        self.registry = AgentRegistry()

        self.dispatcher = AgentDispatcher()



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
        agent_name,
        task
    ):

        agent = self.registry.get(
            agent_name
        )


        if not agent:

            return {

                "status":
                    "agent_not_found",

                "agent":
                    agent_name

            }


        return self.dispatcher.dispatch(
            agent,
            task
        )



    def available_agents(self):

        return self.registry.list_agents()