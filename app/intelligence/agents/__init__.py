"""
Intelligence Agent Package

Provides autonomous agent management
and discovery capabilities.
"""

from .base_agent import BaseAgent
from .agent_metadata import AgentMetadata
from .agent_registry import AgentRegistry


__all__ = [
    "BaseAgent",
    "AgentMetadata",
    "AgentRegistry",
]