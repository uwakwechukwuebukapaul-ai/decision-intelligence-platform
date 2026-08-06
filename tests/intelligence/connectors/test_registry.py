"""
Connector registry tests.
"""

from app.intelligence.connectors.connector import Connector
from app.intelligence.connectors.connector_metadata import ConnectorMetadata
from app.intelligence.connectors.connector_registry import ConnectorRegistry


def create_connector(name: str = "example") -> Connector:
    return Connector(
        ConnectorMetadata(
            name=name,
            version="1.0.0",
            description="Example connector",
        )
    )


def test_register_connector():
    registry = ConnectorRegistry()

    connector = create_connector()

    registry.register(connector)

    assert registry.get("example") == connector


def test_unregister_connector():
    registry = ConnectorRegistry()

    connector = create_connector()

    registry.register(connector)

    removed = registry.unregister("example")

    assert removed == connector
    assert registry.get("example") is None


def test_clear_registry():
    registry = ConnectorRegistry()

    registry.register(create_connector("one"))
    registry.register(create_connector("two"))

    registry.clear()

    assert len(registry) == 0


def test_missing_connector_returns_none():
    registry = ConnectorRegistry()

    assert registry.get("missing") is None