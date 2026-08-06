"""
Connector Metadata.

Defines descriptive information for intelligence connectors.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Any


@dataclass(slots=True)
class ConnectorMetadata:
    """
    Metadata describing an intelligence connector.
    """

    name: str
    version: str
    description: str = ""
    provider: str = ""
    connector_type: str = ""

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize connector metadata.
        """

        return {
            "name": self.name,
            "version": self.version,
            "description": self.description,
            "provider": self.provider,
            "connector_type": self.connector_type,
        }