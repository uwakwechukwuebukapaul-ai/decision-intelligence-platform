from app.intelligence.bus.event import Event
from app.intelligence.bus.event_handler import EventHandler
from app.intelligence.bus.intelligence_bus import IntelligenceBus


class CounterHandler(EventHandler):
    def __init__(self):
        self.count = 0

    def handle(self, event):
        self.count += 1


def test_bus_publish():
    bus = IntelligenceBus()

    handler = CounterHandler()

    bus.register(
        "ioc.detected",
        handler,
    )

    executed = bus.publish(
        Event(name="ioc.detected")
    )

    assert executed == 1
    assert handler.count == 1


def test_bus_unregister():
    bus = IntelligenceBus()

    handler = CounterHandler()

    bus.register(
        "ioc.detected",
        handler,
    )

    bus.unregister(
        "ioc.detected",
        handler,
    )

    executed = bus.publish(
        Event(name="ioc.detected")
    )

    assert executed == 0


def test_bus_clear():
    bus = IntelligenceBus()

    bus.register(
        "event",
        CounterHandler(),
    )

    bus.clear()

    assert bus.event_names == []