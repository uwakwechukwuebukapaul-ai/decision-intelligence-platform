"""
Enterprise Plugin Registry.

Stores and manages registered plugins.
"""

from __future__ import annotations

from app.intelligence.plugins.plugin import Plugin


class PluginRegistry:
    """
    Registry of enterprise plugins.
    """

    def __init__(self) -> None:
        self._plugins: dict[str, Plugin] = {}

    def register(
        self,
        plugin: Plugin,
    ) -> None:
        """
        Register a plugin.

        Raises
        ------
        ValueError
            If a plugin with the same name already exists.
        """
        if plugin.name in self._plugins:
            raise ValueError(
                f"Plugin '{plugin.name}' is already registered."
            )

        self._plugins[plugin.name] = plugin

    def unregister(
        self,
        name: str,
    ) -> Plugin | None:
        """
        Remove a plugin from the registry.
        """
        return self._plugins.pop(name, None)

    def get(
        self,
        name: str,
    ) -> Plugin | None:
        """
        Retrieve a plugin by name.
        """
        return self._plugins.get(name)

    def all(self) -> list[Plugin]:
        """
        Return all registered plugins.
        """
        return list(self._plugins.values())

    def clear(self) -> None:
        """
        Remove every plugin.
        """
        self._plugins.clear()

    @property
    def plugin_names(self) -> list[str]:
        """
        Return registered plugin names.
        """
        return sorted(self._plugins.keys())

    def __contains__(
        self,
        name: str,
    ) -> bool:
        return name in self._plugins

    def __len__(self) -> int:
        return len(self._plugins)