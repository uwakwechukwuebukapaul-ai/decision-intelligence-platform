"""
Plugin Base Class

Enterprise plugin abstraction for
Decision Intelligence Platform.
"""

from __future__ import annotations

from .plugin_metadata import PluginMetadata


class Plugin:
    """
    Base plugin.

    Supports both:

    1.
        Plugin(
            metadata=PluginMetadata(...)
        )

    2.
        class MyPlugin(Plugin):
            ...
    """

    def __init__(
        self,
        metadata: PluginMetadata | None = None,
    ):

        self.metadata = metadata

        self.enabled = False

    # ----------------------------
    # Convenience Properties
    # ----------------------------

    @property
    def name(self) -> str:

        if self.metadata:

            return self.metadata.name

        return self.__class__.__name__.lower()

    @property
    def version(self) -> str:

        if self.metadata:

            return self.metadata.version

        return "1.0.0"

    @property
    def description(self) -> str:

        if self.metadata:

            return self.metadata.description

        return ""

    # ----------------------------
    # Lifecycle
    # ----------------------------

    def initialize(self):

        pass

    def shutdown(self):

        pass

    def enable(self):

        self.enabled = True

    def disable(self):

        self.enabled = False