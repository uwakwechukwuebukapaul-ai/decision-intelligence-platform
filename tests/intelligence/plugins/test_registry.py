from app.intelligence.plugins.plugin import Plugin
from app.intelligence.plugins.plugin_metadata import PluginMetadata
from app.intelligence.plugins.plugin_registry import PluginRegistry


def create_plugin(name: str = "example") -> Plugin:
    return Plugin(
        metadata=PluginMetadata(
            name=name,
            version="1.0.0",
            description="Example plugin",
        )
    )


def test_register_plugin():
    registry = PluginRegistry()
    plugin = create_plugin()

    registry.register(plugin)

    assert registry.get("example") is plugin


def test_unregister_plugin():
    registry = PluginRegistry()
    plugin = create_plugin()

    registry.register(plugin)
    registry.unregister("example")

    assert registry.get("example") is None


def test_clear_registry():
    registry = PluginRegistry()

    registry.register(create_plugin("plugin1"))
    registry.register(create_plugin("plugin2"))

    registry.clear()

    assert registry.all() == []


def test_missing_plugin_returns_none():
    registry = PluginRegistry()

    assert registry.get("missing") is None