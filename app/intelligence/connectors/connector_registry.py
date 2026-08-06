"""
Enterprise Connector Registry.

Stores and manages registered intelligence connectors.
"""

from __future__ import annotations

from app.intelligence.connectors.connector import Connector


class ConnectorRegistry:
    """
    Registry for intelligence connectors.
    """

    def __init__(self) -> None:
        self._connectors: dict[str, Connector] = {}

    def register(
        self,
        connector: Connector,
    ) -> None:
        """
        Register a connector.
        """

        if connector.name in self._connectors:
            raise ValueError(
                f"Connector '{connector.name}' already registered."
            )

        self._connectors[connector.name] = connector

    def unregister(
        self,
        name: str,
    ) -> Connector | None:
        """
        Remove connector from registry.
        """

        return self._connectors.pop(name, None)

    def get(
        self,
        name: str,
    ) -> Connector | None:
        """
        Retrieve connector by name.
        """

        return self._connectors.get(name)

    def all(self) -> list[Connector]:
        """
        Return all registered connectors.
        """

        return list(self._connectors.values())

    def clear(self) -> None:
        """
        Remove all connectors.
        """

        self._connectors.clear()

    @property
    def connector_names(self) -> list[str]:
        """
        Return connector names.
        """

        return sorted(self._connectors.keys())

    def __contains__(
        self,
        name: str,
    ) -> bool:
        return name in self._connectors

    def __len__(self) -> int:
        return len(self._connectors)