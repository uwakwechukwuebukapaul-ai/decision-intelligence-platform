"""
Sentinel DNA - Orchestration Schemas
"""


from dataclasses import dataclass
from typing import Any



@dataclass
class InvestigationResult:

    indicator: str

    intelligence: dict[str, Any]

    reasoning: dict[str, Any]

    copilot: dict[str, Any]

    created_at: str