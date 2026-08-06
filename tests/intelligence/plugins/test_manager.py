from app.intelligence.plugins.plugin import Plugin
from app.intelligence.plugins.plugin_manager import PluginManager


class DemoPlugin(Plugin):
    @property
    def name(self) -> str:
        return "demo"

    def initialize(self) -> None:
        pass

    def shutdown(self) -> None:
        pass


def test_manager_register_and_get():
    manager = PluginManager()

    plugin = DemoPlugin()

    manager.register(plugin)

    assert manager.get("demo") is plugin


def test_manager_unregister():
    manager = PluginManager()

    plugin = DemoPlugin()

    manager.register(plugin)
    manager.unregister("demo")

    assert manager.get("demo") is None


def test_manager_list_plugins():
    manager = PluginManager()

    manager.register(DemoPlugin())

    plugins = manager.list_plugins()

    assert len(plugins) == 1
    assert plugins[0].name == "demo"


def test_manager_clear():
    manager = PluginManager()

    manager.register(DemoPlugin())

    manager.clear()

    assert manager.list_plugins() == []