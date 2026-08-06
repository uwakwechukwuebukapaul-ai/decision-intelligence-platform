"""
Enterprise Plugin Base Class.
"""

from __future__ import annotations

from abc import ABC
from abc import abstractmethod

from app.intelligence.plugins.plugin_metadata import PluginMetadata


class Plugin(ABC):
    """
    Base class for all Intelligence Platform plugins.
    """

    def __init__(
        self,
        metadata: PluginMetadata,
    ) -> None:
        self._metadata = metadata
        self._enabled = False

    @property
    def metadata(self) -> PluginMetadata:
        return self._metadata

    @property
    def name(self) -> str:
        return self._metadata.name

    @property
    def version(self) -> str:
        return self._metadata.version

    @property
    def enabled(self) -> bool:
        return self._enabled

    def enable(self) -> None:
        if not self._enabled:
            self.initialize()
            self._enabled = True

    def disable(self) -> None:
        if self._enabled:
            self.shutdown()
            self._enabled = False

    @abstractmethod
    def initialize(self) -> None:
        """
        Initialize plugin resources.
        """
        raise NotImplementedError

    @abstractmethod
    def shutdown(self) -> None:
        """
        Release plugin resources.
        """
        raise NotImplementedError