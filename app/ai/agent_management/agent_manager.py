from app.ai.agent_management.agent_registry import AgentRegistry
from app.ai.agent_management.lifecycle_manager import LifecycleManager



class AgentManager:
    """
    Central manager for autonomous agent operations.
    """


    def __init__(self):

        self.registry = AgentRegistry()

        self.lifecycle = LifecycleManager()



    def register_agent(self, agent_id, metadata=None):

        return self.registry.register_agent(
            agent_id,
            metadata
        )



    def list_agents(self):

        return self.registry.get_agents()



    def start_agent(self, agent_id):

        return self.lifecycle.start_agent(
            agent_id
        )



    def stop_agent(self, agent_id):

        return self.lifecycle.stop_agent(
            agent_id
        )