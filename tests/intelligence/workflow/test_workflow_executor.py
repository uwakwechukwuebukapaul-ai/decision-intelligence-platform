from app.intelligence.workflow.workflow_executor import (
    WorkflowExecutor,
)

from app.intelligence.workflow.workflow_context import (
    WorkflowContext,
)

from app.intelligence.coordination.workflow import (
    Workflow,
    WorkflowStep,
)


def test_workflow_executor_completes_workflow():

    workflow = Workflow(
        name="Investigation",
        description="SOC investigation",
    )

    workflow.add_step(
        WorkflowStep(
            name="IOC Analysis",
            capability="ioc_lookup",
        )
    )


    context = WorkflowContext(
        workflow_id="WF-001"
    )


    executor = WorkflowExecutor()

    result = executor.execute(
        workflow,
        context,
    )


    assert result.success()
    assert result.state == "COMPLETED"
    assert "IOC Analysis" in result.data