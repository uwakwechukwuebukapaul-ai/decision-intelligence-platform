from .agent_registry import AgentRegistry
from .agent_executor import AgentExecutor
from .agent_memory import AgentMemory
from .agent_reasoner import AgentReasoner
from .agent_supervisor import AgentSupervisor


class AIAgentRuntime:


    def __init__(self):

        self.registry = AgentRegistry()

        self.executor = AgentExecutor()

        self.memory = AgentMemory()

        self.reasoner = AgentReasoner()

        self.supervisor = AgentSupervisor()



    def register_agent(self, name, agent):

        return self.registry.register_agent(
            name,
            agent
        )



    def execute(self, agent_name, task):

        agent = self.registry.get_agent(agent_name)


        if not agent:

            return {
                "status":"error",
                "message":"Agent not found"
            }


        result = self.executor.execute(
            agent,
            task
        )


        self.memory.store(result)

        return result



    def reason(self, context):

        return self.reasoner.analyze(
            context
        )