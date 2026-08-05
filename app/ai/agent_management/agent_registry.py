"""
Agent Management Registry

Production registry for autonomous agents.
Handles registration, discovery, lifecycle tracking,
and autonomous workforce management.
"""

from datetime import datetime, UTC


class AgentRegistry:

    def __init__(self):
        self.agents = {}


    def _timestamp(self):
        return datetime.now(UTC).isoformat()


    def register_agent(
        self,
        agent_id=None,
        name=None,
        capability=None,
        status="active",
        agent_type=None,
        metadata=None,
        **kwargs
    ):

        timestamp = self._timestamp()

        agent = {
            "agent_id": agent_id,
            "name": name,
            "capability": capability,
            "agent_type": agent_type,
            "status": status,
            "metadata": metadata or {},
            "created_at": timestamp,
            "updated_at": timestamp,
        }

        self.agents[agent_id] = agent

        return agent


    def get_agent(self, agent_id):

        return self.agents.get(agent_id)


    def list_agents(self):

        return list(self.agents.values())


    def update_agent_status(
        self,
        agent_id,
        status
    ):

        agent = self.agents.get(agent_id)

        if not agent:
            return None

        agent["status"] = status
        agent["updated_at"] = self._timestamp()

        return agent


    def remove_agent(
        self,
        agent_id
    ):

        return self.agents.pop(
            agent_id,
            None
        )


    def count(self):

        return len(self.agents)



agent_registry = AgentRegistry()