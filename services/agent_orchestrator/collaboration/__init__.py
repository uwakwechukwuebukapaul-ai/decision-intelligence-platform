"""
Sentinel DNA Agent Collaboration Layer

Responsible for:
- Agent-to-agent communication
- Multi-agent workflows
- Investigation coordination
"""

from .agent_message import AgentMessage
from .collaboration_engine import CollaborationEngine
from .workflow_manager import WorkflowManager


__all__ = [
    "AgentMessage",
    "CollaborationEngine",
    "WorkflowManager"
]