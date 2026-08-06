"""
Sentinel DNA - Investigation Task Schema
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass
class InvestigationTask:

    task_id: str

    indicator: str

    status: str = "created"

    priority: str = "medium"

    result: dict[str, Any] = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )
