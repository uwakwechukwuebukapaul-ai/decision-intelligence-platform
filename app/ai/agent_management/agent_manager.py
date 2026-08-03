"""
Agent Manager v49

Controls:
- Agent creation
- Workforce bootstrap
- Registry integration
"""


from app.ai.agent_management.agent_registry import (
    AgentRegistry
)


from app.ai.agents.decision_agent import (
    DecisionAgent
)


from app.ai.agents.forecasting_agent import (
    ForecastingAgent
)


from app.ai.agents.research_agent import (
    ResearchAgent
)



class AgentManager:


    def __init__(self):

        self.registry = AgentRegistry()


        self.bootstrap_workforce()



    # =====================================
    # Bootstrap Default Workforce
    # =====================================

    def bootstrap_workforce(self):

        agents = [

            DecisionAgent(),

            ForecastingAgent(),

            ResearchAgent()

        ]


        for agent in agents:

            profile = agent.profile()


            self.registry.register_agent(

                name=profile["name"],

                agent_type=profile["type"],

                capabilities=profile["capabilities"]

            )



    # =====================================
    # List Agents
    # =====================================

    def list_agents(self):

        return self.registry.list_agents()



    # =====================================
    # Create Agent
    # =====================================

    def create_agent(
        self,
        name,
        agent_type,
        capabilities=None
    ):

        return self.registry.register_agent(

            name,

            agent_type,

            capabilities

        )