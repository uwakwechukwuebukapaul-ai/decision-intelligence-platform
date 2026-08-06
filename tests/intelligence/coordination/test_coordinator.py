"""
Coordinator Tests

Tests intelligence workflow
orchestration.
"""

from app.intelligence.coordination.workflow import (
    Workflow,
    WorkflowStep,
)

from app.intelligence.coordination.execution_plan import (
    ExecutionPlan,
)

from app.intelligence.coordination.coordinator import (
    Coordinator,
)


class FakeAgent:

    def __init__(self, name, capabilities):

        self.metadata = type(
            "Metadata",
            (),
            {
                "name": name,
                "capabilities": capabilities,
            },
        )


    def execute(
        self,
        payload,
    ):

        return {
            "message": "executed",
            "payload": payload,
        }



class FakeRegistry:

    def __init__(self):

        agent = FakeAgent(
            "Threat Intelligence Agent",
            [
                "threat_intelligence",
                "risk_analysis",
            ],
        )

        self.agents = {
            "threat_agent": agent
        }



from app.intelligence.runtime.agent_executor import (
    AgentExecutor,
)



def test_coordinator_executes_workflow():

    workflow = Workflow(
        "SOC Investigation",
        "Threat investigation workflow",
    )


    workflow.add_step(
        WorkflowStep(
            name="Threat Analysis",
            capability="threat_intelligence",
            payload={
                "ioc": "example.com"
            },
        )
    )


    workflow.add_step(
        WorkflowStep(
            name="Risk Assessment",
            capability="risk_analysis",
            depends_on=[
                "Threat Analysis"
            ],
        )
    )


    executor = AgentExecutor(
        FakeRegistry()
    )


    coordinator = Coordinator(
        executor
    )


    result = coordinator.execute(
        ExecutionPlan(workflow)
    )


    assert result["summary"]["total"] == 2

    assert (
        result["summary"]["successful"]
        == 2
    )



def test_coordinator_returns_results():

    workflow = Workflow(
        "Simple Workflow",
        "Testing results",
    )


    workflow.add_step(
        WorkflowStep(
            "Threat Scan",
            "threat_intelligence",
        )
    )


    coordinator = Coordinator(
        AgentExecutor(
            FakeRegistry()
        )
    )


    result = coordinator.execute(
        ExecutionPlan(workflow)
    )


    assert len(
        result["results"]
    ) == 1


    assert (
        result["results"][0]["execution"]["status"]
        == "completed"
    )