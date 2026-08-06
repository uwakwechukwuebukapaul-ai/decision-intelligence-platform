"""
Enterprise Event Handler.

Base class for Intelligence Bus event handlers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from app.intelligence.bus.event import Event


class EventHandler(ABC):
    """
    Base class for all event handlers.
    """

    @abstractmethod
    def handle(self, event: Event) -> None:
        """
        Process an event.
        """
        raise NotImplementedError