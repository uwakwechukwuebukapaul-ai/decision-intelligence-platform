"""
Connector manager tests.
"""

from app.intelligence.connectors.connector import Connector
from app.intelligence.connectors.connector_metadata import ConnectorMetadata
from app.intelligence.connectors.connector_manager import ConnectorManager


def create_connector(name: str = "example") -> Connector:
    return Connector(
        ConnectorMetadata(
            name=name,
            version="1.0.0",
            description="Example connector",
        )
    )


def test_manager_register_and_get():
    manager = ConnectorManager()

    connector = create_connector()

    manager.register(connector)

    assert manager.get("example") == connector


def test_manager_unregister():
    manager = ConnectorManager()

    connector = create_connector()

    manager.register(connector)

    removed = manager.unregister("example")

    assert removed == connector
    assert manager.get("example") is None


def test_manager_list_connectors():
    manager = ConnectorManager()

    manager.register(
        create_connector()
    )

    connectors = manager.list_connectors()

    assert len(connectors) == 1
    assert connectors[0].name == "example"


def test_manager_connect_all():
    manager = ConnectorManager()

    connector = create_connector()

    manager.register(connector)

    manager.connect_all()

    assert connector.connected


def test_manager_disconnect_all():
    manager = ConnectorManager()

    connector = create_connector()

    manager.register(connector)

    manager.connect_all()
    manager.disconnect_all()

    assert not connector.connected


def test_manager_clear():
    manager = ConnectorManager()

    manager.register(
        create_connector()
    )

    manager.clear()

    assert manager.list_connectors() == []