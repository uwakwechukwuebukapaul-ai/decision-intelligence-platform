"""
AI Agent Communication Layer

Provides communication infrastructure
between autonomous AI agents.
"""

from .message_bus import MessageBus
from .communication_engine import CommunicationEngine


__all__ = [
    "MessageBus",
    "CommunicationEngine"
]