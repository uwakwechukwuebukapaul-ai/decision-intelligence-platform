from app.intelligence.planning import (
    IntelligencePlanner,
    WorkflowGenerator,
)



def test_planner_creates_strategy():

    planner = IntelligencePlanner()


    strategy = planner.create_strategy(
        "Investigate threat activity"
    )


    assert (
        "threat_intelligence"
        in strategy.capabilities
    )



def test_workflow_generation():

    planner = IntelligencePlanner()


    strategy = planner.create_strategy(
        "Perform threat investigation"
    )


    generator = WorkflowGenerator()


    workflow = generator.generate(
        strategy
    )


    assert workflow.step_count() >= 1

    assert (
        workflow.steps[0].capability
        == "threat_intelligence"
    )