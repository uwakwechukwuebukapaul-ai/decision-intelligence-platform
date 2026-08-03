"""
Agent Registry Engine v49

Responsible for:
- Agent registration
- Agent discovery
- Agent metadata storage
- Agent state tracking

This is the foundation layer for the Autonomous Agent Workforce.
"""


from datetime import datetime
import uuid


class AgentRegistry:
    """
    Central registry for autonomous agents.
    """

    def __init__(self):

        self.agents = {}


    # =====================================
    # Register Agent
    # =====================================

    def register_agent(
        self,
        name,
        agent_type,
        capabilities=None
    ):

        agent_id = (
            "AGENT-"
            + str(uuid.uuid4())[:8].upper()
        )


        agent = {

            "agent_id":
                agent_id,


            "name":
                name,


            "type":
                agent_type,


            "capabilities":
                capabilities or [],


            "status":
                "active",


            "created_at":
                datetime.utcnow().isoformat(),


            "last_seen":
                datetime.utcnow().isoformat()

        }


        self.agents[agent_id] = agent


        return agent



    # =====================================
    # Get Agent
    # =====================================

    def get_agent(
        self,
        agent_id
    ):

        return self.agents.get(
            agent_id
        )



    # =====================================
    # List Agents
    # =====================================

    def list_agents(
        self
    ):

        return list(
            self.agents.values()
        )



    # =====================================
    # Update Agent Status
    # =====================================

    def update_status(
        self,
        agent_id,
        status
    ):

        agent = self.get_agent(
            agent_id
        )


        if not agent:
            return None


        agent["status"] = status


        agent["last_seen"] = (
            datetime.utcnow()
            .isoformat()
        )


        return agent



    # =====================================
    # Remove Agent
    # =====================================

    def remove_agent(
        self,
        agent_id
    ):

        if agent_id in self.agents:

            del self.agents[agent_id]

            return True


        return False