"""
Multi Agent Intelligence Package

Provides autonomous agent collaboration,
communication and coordination capabilities.
"""

from app.ai.multi_agent.communication_bus import CommunicationBus
from app.ai.multi_agent.agent_coordinator import AgentCoordinator


__all__ = [
    "CommunicationBus",
    "AgentCoordinator"
]