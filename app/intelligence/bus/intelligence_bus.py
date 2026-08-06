"""
Enterprise Intelligence Bus.

Public interface for publishing Intelligence events.
"""

from __future__ import annotations

from app.intelligence.bus.event import Event
from app.intelligence.bus.event_dispatcher import EventDispatcher
from app.intelligence.bus.event_handler import EventHandler
from app.intelligence.bus.event_registry import EventRegistry


class IntelligenceBus:
    """
    Enterprise event bus.

    Provides a simple interface for registering handlers
    and publishing events.
    """

    def __init__(self) -> None:
        self._registry = EventRegistry()
        self._dispatcher = EventDispatcher(self._registry)

    def register(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:
        """
        Register an event handler.
        """
        self._registry.register(event_name, handler)

    def unregister(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:
        """
        Remove an event handler.
        """
        self._registry.unregister(event_name, handler)

    def publish(
        self,
        event: Event,
    ) -> int:
        """
        Publish an event.

        Returns
        -------
        int
            Number of handlers executed.
        """
        return self._dispatcher.dispatch(event)

    def clear(self) -> None:
        """
        Remove every registered handler.
        """
        self._registry.clear()

    @property
    def event_names(self) -> list[str]:
        """
        Return all registered event names.
        """
        return self._registry.event_names