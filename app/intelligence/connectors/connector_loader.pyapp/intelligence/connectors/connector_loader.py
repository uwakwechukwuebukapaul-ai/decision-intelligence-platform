"""
Connector Loader.

Responsible for loading and unloading connector instances.
"""

from __future__ import annotations

from typing import Dict, List

from app.intelligence.connectors.connector import Connector


class ConnectorLoader:
    """
    Runtime connector loader.

    Maintains loaded connector instances.
    """

    def __init__(self) -> None:
        self._loaded: Dict[str, Connector] = {}

    def load(
        self,
        connector: Connector,
    ) -> Connector:
        """
        Load a connector instance.
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
        Remove a loaded connector.
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
        Retrieve loaded connector.
        """

        return self._loaded.get(name)

    def list_loaded(self) -> List[Connector]:
        """
        Return loaded connectors.
        """

        return list(self._loaded.values())

    def clear(self) -> None:
        """
        Remove all loaded connectors.
        """

        for connector in self._loaded.values():
            connector.disconnect()

        self._loaded.clear()