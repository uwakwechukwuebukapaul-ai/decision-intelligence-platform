"""
Tests for Runtime Agent Execution
"""


from app.intelligence.runtime import IntelligenceJob
from app.intelligence.runtime.agent_executor import AgentExecutor

from app.intelligence.agents import (
    BaseAgent,
    AgentRegistry,
)



class ThreatIntelligenceAgent(BaseAgent):


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

            "analysis":
                "IOC investigation completed",

            "ioc":
                payload.get("ioc")

        }



def test_agent_execution_success():

    registry = AgentRegistry()


    agent = ThreatIntelligenceAgent()


    registry.register(
        agent
    )


    executor = AgentExecutor(
        registry
    )


    job = IntelligenceJob(
        "threat_intelligence",
        {
            "ioc":
                "malicious-domain.com"
        }
    )


    result = executor.execute(
        job
    )


    assert result["status"] == "completed"

    assert (
        result["agent"]
        ==
        "Threat Intelligence Agent"
    )

    assert (
        job.status
        ==
        "completed"
    )



def test_agent_execution_failure():

    registry = AgentRegistry()


    executor = AgentExecutor(
        registry
    )


    job = IntelligenceJob(
        "unknown_capability"
    )


    result = executor.execute(
        job
    )


    assert result["status"] == "failed"

    assert (
        job.status
        ==
        "failed"
    )