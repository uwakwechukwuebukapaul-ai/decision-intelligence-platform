"""
Sentinel DNA Agent Factory

Responsible for:
- Loading autonomous agents
- Registering specialized SOC agents
- Providing agent discovery
"""

from .agent_loader import AgentLoader
from .default_agents import load_default_agents


__all__ = [
    "AgentLoader",
    "load_default_agents"
]