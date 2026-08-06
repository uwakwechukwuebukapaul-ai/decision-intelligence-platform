"""
Enterprise Plugin Metadata.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(slots=True, frozen=True)
class PluginMetadata:
    """
    Immutable metadata describing a plugin.
    """

    name: str
    version: str
    author: str = ""
    description: str = ""

    def to_dict(self) -> dict[str, str]:
        return {
            "name": self.name,
            "version": self.version,
            "author": self.author,
            "description": self.description,
        }