"""
AI Agent Orchestrator

Coordinates SOC agents.
"""


from .agent_registry import AgentRegistry
from .investigation_agent import InvestigationAgent
from .hunting_agent import HuntingAgent



class AgentOrchestrator:


    def __init__(self):

        self.registry = AgentRegistry()

        self.registry.register(
            InvestigationAgent()
        )

        self.registry.register(
            HuntingAgent()
        )



    def run(
        self,
        context
    ):


        results = []


        for agent_name in self.registry.list_agents():

            agent = self.registry.get(
                agent_name
            )

            results.append(

                agent.execute(
                    context
                )

            )


        return {

            "agents_executed":
                len(results),

            "results":
                results

        }