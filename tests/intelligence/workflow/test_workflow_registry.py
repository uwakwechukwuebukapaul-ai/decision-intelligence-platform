from app.intelligence.workflow.workflow_registry import (
    WorkflowRegistry,
)

from app.intelligence.coordination.workflow import (
    Workflow,
)


def test_workflow_registry_register_and_get():

    registry = WorkflowRegistry()

    workflow = Workflow(
        name="Test Workflow",
        description="Testing registry",
    )

    registry.register(workflow)

    result = registry.get(
        "Test Workflow"
    )

    assert result is workflow


def test_workflow_registry_list():

    registry = WorkflowRegistry()

    workflow = Workflow(
        name="Workflow A",
        description="Example",
    )

    registry.register(workflow)

    assert "Workflow A" in registry.list()