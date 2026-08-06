"""
Connector Manager.

High-level service for managing intelligence connectors.
"""

from __future__ import annotations

from app.intelligence.connectors.connector import Connector
from app.intelligence.connectors.connector_registry import ConnectorRegistry
from app.intelligence.connectors.connector_loader import ConnectorLoader


class ConnectorManager:
    """
    Coordinates connector registration, retrieval,
    lifecycle, and loading.
    """

    def __init__(self) -> None:
        self._registry = ConnectorRegistry()
        self._loader = ConnectorLoader()

    @property
    def registry(self) -> ConnectorRegistry:
        return self._registry

    @property
    def loader(self) -> ConnectorLoader:
        return self._loader

    def register(
        self,
        connector: Connector,
    ) -> None:
        """
        Register connector.
        """

        self._registry.register(connector)

    def unregister(
        self,
        name: str,
    ) -> Connector | None:
        """
        Remove connector.
        """

        return self._registry.unregister(name)

    def get(
        self,
        name: str,
    ) -> Connector | None:
        """
        Retrieve connector.
        """

        return self._registry.get(name)

    def list_connectors(self) -> list[Connector]:
        """
        Return all connectors.
        """

        return self._registry.all()

    def connect_all(self) -> None:
        """
        Activate all registered connectors.
        """

        for connector in self._registry.all():
            connector.connect()

    def disconnect_all(self) -> None:
        """
        Disconnect all connectors.
        """

        for connector in self._registry.all():
            connector.disconnect()

    def clear(self) -> None:
        """
        Clear connector system.
        """

        self._registry.clear()
        self._loader.clear()