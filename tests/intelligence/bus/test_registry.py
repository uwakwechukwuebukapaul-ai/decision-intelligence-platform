from app.intelligence.bus.event_handler import EventHandler
from app.intelligence.bus.event_registry import EventRegistry


class DummyHandler(EventHandler):
    def handle(self, event):
        pass


def test_register_handler():
    registry = EventRegistry()
    handler = DummyHandler()

    registry.register("alert.created", handler)

    handlers = registry.get_handlers("alert.created")

    assert len(handlers) == 1
    assert handlers[0] is handler


def test_unregister_handler():
    registry = EventRegistry()
    handler = DummyHandler()

    registry.register("alert.created", handler)
    registry.unregister("alert.created", handler)

    assert registry.get_handlers("alert.created") == []


def test_clear_registry():
    registry = EventRegistry()

    registry.register("a", DummyHandler())
    registry.register("b", DummyHandler())

    registry.clear()

    assert registry.event_names == []