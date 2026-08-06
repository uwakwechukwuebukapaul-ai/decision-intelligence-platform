from __future__ import annotations

from .plugin import Plugin


class PluginRegistry:
    """
    Stores loaded plugins.
    """

    def __init__(self):
        self._plugins: dict[str, Plugin] = {}

    def register(self, plugin: Plugin) -> None:
        self._plugins[plugin.name] = plugin

    def unregister(self, name: str) -> None:
        self._plugins.pop(name, None)

    def get(self, name: str):
        return self._plugins.get(name)

    def all(self):
        return list(self._plugins.values())

    def clear(self):
        self._plugins.clear()