from app.intelligence.bus.event import Event
from app.intelligence.bus.event_dispatcher import EventDispatcher
from app.intelligence.bus.event_handler import EventHandler
from app.intelligence.bus.event_registry import EventRegistry


class CounterHandler(EventHandler):
    def __init__(self):
        self.count = 0

    def handle(self, event):
        self.count += 1


def test_dispatch_calls_handlers():
    registry = EventRegistry()

    handler = CounterHandler()

    registry.register("case.created", handler)

    dispatcher = EventDispatcher(registry)

    executed = dispatcher.dispatch(
        Event(name="case.created")
    )

    assert executed == 1
    assert handler.count == 1


def test_dispatch_unknown_event():
    registry = EventRegistry()

    dispatcher = EventDispatcher(registry)

    executed = dispatcher.dispatch(
        Event(name="unknown")
    )

    assert executed == 0