"""
Connector Loader.

Responsible for runtime connector lifecycle management.
"""

from __future__ import annotations

from typing import Dict, List

from app.intelligence.connectors.connector import Connector


class ConnectorLoader:
    """
    Loads and manages connector instances.
    """

    def __init__(self) -> None:
        self._loaded: Dict[str, Connector] = {}

    def load(
        self,
        connector: Connector,
    ) -> Connector:
        """
        Load connector instance.
        """

        name = connector.metadata.name

        self._loaded[name] = connector

        connector.connect()

        return connector

    def unload(
        self,
        name: str,
    ) -> bool:
        """
        Unload connector.
        """

        connector = self._loaded.get(name)

        if connector is None:
            return False

        connector.disconnect()

        del self._loaded[name]

        return True

    def get(
        self,
        name: str,
    ) -> Connector | None:
        """
        Get loaded connector.
        """

        return self._loaded.get(name)

    def list_loaded(self) -> List[Connector]:
        """
        List loaded connectors.
        """

        return list(self._loaded.values())

    def clear(self) -> None:
        """
        Clear all connectors.
        """

        for connector in self._loaded.values():
            connector.disconnect()

        self._loaded.clear()