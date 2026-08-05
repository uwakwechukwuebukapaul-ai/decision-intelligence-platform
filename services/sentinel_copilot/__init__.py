"""
Sentinel DNA AI Copilot Layer

Provides:
- Natural language security assistance
- Investigation guidance
- Intelligence retrieval
- Analyst recommendations
"""

from .copilot_engine import CopilotEngine
from .query_parser import QueryParser
from .response_generator import ResponseGenerator
from .investigation_assistant import InvestigationAssistant


__all__ = [
    "CopilotEngine",
    "QueryParser",
    "ResponseGenerator",
    "InvestigationAssistant"
]