from app.core.container import (
    ServiceContainer,
)


def test_container_initialization():

    container = ServiceContainer()

    container.initialize()

    assert container._initialized is True

    assert container.task_manager is not None

    assert container.policy_engine is not None

    assert container.capability_manager is not None

    assert container.audit_logger is not None

    assert container.intelligence_controller is not None



def test_container_health():

    container = ServiceContainer()

    container.initialize()

    health = container.health()

    assert health["container"] == "healthy"