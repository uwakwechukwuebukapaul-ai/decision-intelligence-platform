"""
Connector loader tests.
"""

from app.intelligence.connectors.connector import Connector
from app.intelligence.connectors.connector_metadata import ConnectorMetadata
from app.intelligence.connectors.connector_loader import ConnectorLoader


def create_connector() -> Connector:
    return Connector(
        ConnectorMetadata(
            name="example",
            version="1.0.0",
            description="Example connector",
        )
    )


def test_loader_loads_connector():
    loader = ConnectorLoader()

    connector = create_connector()

    result = loader.load(connector)

    assert result is connector


def test_loader_unloads_connector():
    loader = ConnectorLoader()

    connector = create_connector()

    loader.load(connector)

    result = loader.unload("example")

    assert result is True


def test_loader_missing_connector():
    loader = ConnectorLoader()

    result = loader.unload("missing")

    assert result is False


def test_loader_list_loaded():
    loader = ConnectorLoader()

    connector = create_connector()

    loader.load(connector)

    connectors = loader.list_loaded()

    assert len(connectors) == 1
    assert connectors[0].name == "example"