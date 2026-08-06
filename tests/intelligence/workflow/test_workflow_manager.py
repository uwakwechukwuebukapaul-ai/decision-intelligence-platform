from app.intelligence.workflow.workflow_manager import (
    WorkflowManager,
)

from app.intelligence.coordination.workflow import (
    Workflow,
)


def test_workflow_manager_run():

    manager = WorkflowManager()


    workflow = Workflow(
        name="Threat Investigation",
        description="Analyze threat",
    )


    manager.register(
        workflow
    )


    result = manager.run(
        workflow_name="Threat Investigation",
        workflow_id="INC-001",
    )


    assert result.success()
    assert result.workflow_id == "INC-001"