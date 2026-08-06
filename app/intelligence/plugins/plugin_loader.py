"""
Enterprise Plugin Loader.

Loads plugins into the Plugin Registry.
"""

from __future__ import annotations

from collections.abc import Iterable

from app.intelligence.plugins.plugin import Plugin
from app.intelligence.plugins.plugin_registry import PluginRegistry


class PluginLoader:
    """
    Loads plugins into the registry.
    """

    def __init__(
        self,
        registry: PluginRegistry,
    ) -> None:
        self._registry = registry

    def load(
        self,
        plugin: Plugin,
    ) -> Plugin:
        """
        Load a single plugin.

        Returns
        -------
        Plugin
            The registered plugin.
        """
        self._registry.register(plugin)
        return plugin

    def load_many(
        self,
        plugins: Iterable[Plugin],
    ) -> list[Plugin]:
        """
        Load multiple plugins.

        Returns
        -------
        list[Plugin]
            Registered plugins.
        """
        loaded: list[Plugin] = []

        for plugin in plugins:
            self._registry.register(plugin)
            loaded.append(plugin)

        return loaded