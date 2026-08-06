"""
Connector tests.
"""

from app.intelligence.connectors.connector import Connector
from app.intelligence.connectors.connector_metadata import ConnectorMetadata


def create_connector() -> Connector:
    return Connector(
        ConnectorMetadata(
            name="example_connector",
            version="1.0.0",
            description="Example connector",
            provider="Sentinel DNA",
            connector_type="test",
        )
    )


def test_connector_initializes():
    connector = create_connector()

    assert connector.name == "example_connector"
    assert connector.version == "1.0.0"
    assert not connector.connected


def test_connector_connect():
    connector = create_connector()

    connector.connect()

    assert connector.connected
    assert connector.health_check()


def test_connector_disconnect():
    connector = create_connector()

    connector.connect()
    connector.disconnect()

    assert not connector.connected


def test_connector_execute():
    connector = create_connector()

    result = connector.execute(
        {"action": "analyze"}
    )

    assert result["connector"] == "example_connector"
    assert result["status"] == "executed"