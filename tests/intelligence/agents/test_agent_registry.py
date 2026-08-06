"""
Tests for Intelligence Agent Registry
"""


from app.intelligence.agents import (
    BaseAgent,
    AgentRegistry,
)



class ThreatAgent(BaseAgent):


    def __init__(self):

        super().__init__(
            name="Threat Intelligence Agent",
            version="1.0.0",
            capabilities=[
                "threat_intelligence"
            ],
        )


    def execute(
        self,
        payload,
    ):

        return {

            "result":
                "Threat analysis complete"

        }



def test_register_agent():


    registry = AgentRegistry()


    agent = ThreatAgent()


    registry.register(
        agent
    )


    assert (
        "Threat Intelligence Agent"
        in registry.list_agents()
    )



def test_execute_registered_agent():


    registry = AgentRegistry()


    agent = ThreatAgent()


    registry.register(
        agent
    )


    loaded_agent = registry.get(
        "Threat Intelligence Agent"
    )


    result = loaded_agent.execute(
        {
            "ioc":
                "example.com"
        }
    )


    assert (
        result["result"]
        ==
        "Threat analysis complete"
    )



def test_agent_metadata():


    agent = ThreatAgent()


    metadata = agent.get_metadata()


    assert (
        metadata["version"]
        ==
        "1.0.0"
    )


    assert (
        metadata["status"]
        ==
        "active"
    )