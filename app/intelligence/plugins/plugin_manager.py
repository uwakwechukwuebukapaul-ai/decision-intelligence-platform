from __future__ import annotations

from .plugin import Plugin
from .plugin_registry import PluginRegistry


class PluginManager:
    """
    Enterprise Plugin Manager.
    """

    def __init__(self):
        self.registry = PluginRegistry()

    def register(self, plugin: Plugin):
        self.registry.register(plugin)

    def unregister(self, name: str):
        self.registry.unregister(name)

    def get(self, name: str):
        return self.registry.get(name)

    def list_plugins(self):
        return self.registry.all()

    def clear(self):
        self.registry.clear()