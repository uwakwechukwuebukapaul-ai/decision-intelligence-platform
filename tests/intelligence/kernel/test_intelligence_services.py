from app.intelligence.kernel.intelligence_services import IntelligenceServices


class DummyRuntime:
    pass


class DummyGovernance:
    pass


class DummyPlanner:
    pass


class DummyMemory:
    pass


class DummyRegistry:
    pass


def test_services_container_initializes():

    services = IntelligenceServices(
        runtime=DummyRuntime(),
        governance=DummyGovernance(),
        planner=DummyPlanner(),
        memory=DummyMemory(),
        agent_registry=DummyRegistry(),
    )

    assert services.runtime is not None
    assert services.governance is not None
    assert services.planner is not None
    assert services.memory is not None
    assert services.agent_registry is not None