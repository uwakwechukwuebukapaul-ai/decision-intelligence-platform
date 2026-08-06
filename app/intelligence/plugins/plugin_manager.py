"""
Enterprise Plugin Manager.

Coordinates plugin loading, registration, and lifecycle.
"""

from __future__ import annotations

from collections.abc import Iterable

from app.intelligence.plugins.plugin import Plugin
from app.intelligence.plugins.plugin_loader import PluginLoader
from app.intelligence.plugins.plugin_registry import PluginRegistry


class PluginManager:
    """
    Enterprise plugin manager.
    """

    def __init__(self) -> None:
        self._registry = PluginRegistry()
        self._loader = PluginLoader(self._registry)

    def load(
        self,
        plugin: Plugin,
    ) -> Plugin:
        """
        Load a single plugin.
        """
        return self._loader.load(plugin)

    def load_many(
        self,
        plugins: Iterable[Plugin],
    ) -> list[Plugin]:
        """
        Load multiple plugins.
        """
        return self._loader.load_many(plugins)

    def enable(
        self,
        name: str,
    ) -> bool:
        """
        Enable a plugin.

        Returns True if found.
        """
        plugin = self._registry.get(name)

        if plugin is None:
            return False

        plugin.enable()
        return True

    def disable(
        self,
        name: str,
    ) -> bool:
        """
        Disable a plugin.

        Returns True if found.
        """
        plugin = self._registry.get(name)

        if plugin is None:
            return False

        plugin.disable()
        return True

    def get(
        self,
        name: str,
    ) -> Plugin | None:
        """
        Retrieve a plugin.
        """
        return self._registry.get(name)

    def plugins(self) -> list[Plugin]:
        """
        Return all registered plugins.
        """
        return self._registry.all()

    def clear(self) -> None:
        """
        Remove all plugins.
        """
        self._registry.clear()

    @property
    def plugin_names(self) -> list[str]:
        """
        Return registered plugin names.
        """
        return self._registry.plugin_names