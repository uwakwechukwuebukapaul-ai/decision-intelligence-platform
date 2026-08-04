"""
Sentinel DNA AI SOC Copilot Layer

Provides analyst assistance through:
- Security reasoning
- Investigation context
- Memory awareness
- Threat analysis
"""

from .copilot_engine import CopilotEngine
from .copilot_model import CopilotResponse
from .conversation_memory import ConversationMemory
from .security_reasoner import SecurityReasoner


__all__ = [
    "CopilotEngine",
    "CopilotResponse",
    "ConversationMemory",
    "SecurityReasoner"
]