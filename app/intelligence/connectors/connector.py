"""
Enterprise Intelligence Connector.

Base abstraction for external intelligence integrations.
"""

from __future__ import annotations

from app.intelligence.connectors.connector_metadata import ConnectorMetadata


class Connector:
    """
    Base connector implementation.

    Examples:
    - SIEM connector
    - Threat intelligence connector
    - Cloud API connector
    - Ticketing connector
    """

    def __init__(
        self,
        metadata: ConnectorMetadata,
    ) -> None:
        self._metadata = metadata
        self._connected = False

    @property
    def metadata(self) -> ConnectorMetadata:
        return self._metadata

    @property
    def name(self) -> str:
        return self._metadata.name

    @property
    def version(self) -> str:
        return self._metadata.version

    @property
    def connected(self) -> bool:
        return self._connected

    def connect(self) -> None:
        """
        Establish connector connection.
        """

        self._connected = True

    def disconnect(self) -> None:
        """
        Close connector connection.
        """

        self._connected = False

    def health_check(self) -> bool:
        """
        Return connector health state.
        """

        return self._connected

    def execute(
        self,
        payload: dict,
    ) -> dict:
        """
        Execute connector operation.

        Intended to be overridden by specific connectors.
        """

        return {
            "connector": self.name,
            "status": "executed",
            "payload": payload,
        }