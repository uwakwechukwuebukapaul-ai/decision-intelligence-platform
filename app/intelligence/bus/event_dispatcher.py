"""
Enterprise Event Dispatcher.

Dispatches Intelligence Bus events to registered handlers.
"""

from __future__ import annotations

from app.intelligence.bus.event import Event
from app.intelligence.bus.event_registry import EventRegistry


class EventDispatcher:
    """
    Dispatches events to registered handlers.
    """

    def __init__(
        self,
        registry: EventRegistry,
    ) -> None:
        self._registry = registry

    def dispatch(
        self,
        event: Event,
    ) -> int:
        """
        Dispatch an event.

        Returns
        -------
        int
            Number of handlers executed.
        """

        handlers = self._registry.get_handlers(event.name)

        count = 0

        for handler in handlers:
            handler.handle(event)
            count += 1

        return count