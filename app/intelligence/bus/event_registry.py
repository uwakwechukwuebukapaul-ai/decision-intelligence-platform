"""
Enterprise Event Registry.

Maintains mappings between event names and their handlers.
"""

from __future__ import annotations

from collections import defaultdict

from app.intelligence.bus.event_handler import EventHandler


class EventRegistry:
    """
    Registry of Intelligence Bus event handlers.
    """

    def __init__(self) -> None:
        self._handlers: dict[str, list[EventHandler]] = defaultdict(list)

    def register(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:
        """
        Register a handler for an event.
        """
        self._handlers[event_name].append(handler)

    def get_handlers(
        self,
        event_name: str,
    ) -> list[EventHandler]:
        """
        Return handlers registered for an event.
        """
        return list(self._handlers.get(event_name, []))

    def unregister(
        self,
        event_name: str,
        handler: EventHandler,
    ) -> None:
        """
        Remove a handler if present.
        """
        handlers = self._handlers.get(event_name)

        if not handlers:
            return

        if handler in handlers:
            handlers.remove(handler)

        if not handlers:
            self._handlers.pop(event_name, None)

    def clear(self) -> None:
        """
        Remove every registered handler.
        """
        self._handlers.clear()

    @property
    def event_names(self) -> list[str]:
        """
        Return registered event names.
        """
        return sorted(self._handlers.keys())