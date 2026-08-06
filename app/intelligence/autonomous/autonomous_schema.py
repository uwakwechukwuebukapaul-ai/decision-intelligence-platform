"""
Sentinel DNA - Autonomous Investigation Schemas

Defines structured data models for:

- Autonomous investigations
- Decisions
- Agent execution results
- Evidence collection
"""


from __future__ import annotations


from dataclasses import dataclass, field
from datetime import datetime
from typing import Any





@dataclass
class AutonomousInvestigationResult:
    """
    Result returned by autonomous investigation engine.
    """

    indicator: str

    status: str

    confidence: int

    actions: list = field(
        default_factory=list
    )

    evidence: dict = field(
        default_factory=dict
    )

    reasoning: list = field(
        default_factory=list
    )

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )






@dataclass
class AutonomousDecisionResult:
    """
    Decision output from autonomous decision manager.
    """

    indicator: str

    decision: str

    priority: str

    confidence: int

    reasoning: list = field(
        default_factory=list
    )

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )






@dataclass
class AutonomousTaskResult:
    """
    Task execution result.
    """

    task_id: str

    status: str

    result: dict = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat()
    )