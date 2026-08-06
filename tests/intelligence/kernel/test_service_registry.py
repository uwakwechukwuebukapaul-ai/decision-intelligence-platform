from app.intelligence.kernel.service_registry import ServiceRegistry


def test_register_service():

    registry = ServiceRegistry()

    service = object()

    registry.register(
        "runtime",
        service,
    )

    assert registry.get("runtime") is service


def test_missing_service_returns_none():

    registry = ServiceRegistry()

    assert registry.get("missing") is None