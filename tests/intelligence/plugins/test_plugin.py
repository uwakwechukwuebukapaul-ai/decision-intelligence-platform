from app.intelligence.plugins.plugin import Plugin
from app.intelligence.plugins.plugin_metadata import PluginMetadata


def create_plugin() -> Plugin:
    return Plugin(
        metadata=PluginMetadata(
            name="example",
            version="1.0.0",
            description="Example plugin",
        )
    )


def test_plugin_initializes():
    plugin = create_plugin()

    assert plugin.name == "example"
    assert plugin.version == "1.0.0"
    assert plugin.enabled is False


def test_plugin_enable():
    plugin = create_plugin()

    plugin.enable()

    assert plugin.enabled is True


def test_plugin_disable():
    plugin = create_plugin()

    plugin.enable()
    plugin.disable()

    assert plugin.enabled is False