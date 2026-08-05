from .agent_registry import AgentRegistry
from .agent_executor import AgentExecutor
from .agent_memory import AgentMemory
from .task_router import TaskRouter



class AgentOrchestrator:
    """
    Central coordination engine for
    Sentinel DNA autonomous agents.
    """


    def __init__(self):

        self.registry = AgentRegistry()

        self.executor = AgentExecutor()

        self.memory = AgentMemory()

        self.router = TaskRouter()



    def register_agent(
        self,
        name,
        agent
    ):

        self.registry.register(
            name,
            agent
        )



    def execute_task(
        self,
        task_type,
        task
    ):

        agent_name = self.router.route(
            task_type
        )


        agent = self.registry.get(
            agent_name
        )


        if not agent:

            return {

                "status": "failed",

                "message":
                f"No agent registered for {task_type}"

            }


        result = self.executor.execute(
            agent,
            task
        )


        self.memory.remember(
            agent_name,
            {
                "task": task,
                "result": result
            }
        )


        return {

            "agent":
            agent_name,

            "result":
            result

        }



    def status(self):

        return {

            "agents":
            self.registry.list_agents(),

            "memory_agents":
            list(
                self.memory.memory.keys()
            )

        }