"""
Sentinel DNA - Fusion Intelligence Schema
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any



@dataclass
class FusionResult:
    """
    Unified intelligence investigation result.
    """

    indicator: str

    risk: dict[str, Any] = field(default_factory=dict)

    correlation: dict[str, Any] = field(default_factory=dict)

    campaign: dict[str, Any] = field(default_factory=dict)

    threat_actor: dict[str, Any] = field(default_factory=dict)

    graph: dict[str, Any] = field(default_factory=dict)

    memory: list[dict[str, Any]] = field(default_factory=list)

    recommendation: dict[str, Any] = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )


    def to_dict(self):

        return {

            "indicator": self.indicator,

            "risk": self.risk,

            "correlation": self.correlation,

            "campaign": self.campaign,

            "threat_actor": self.threat_actor,

            "graph": self.graph,

            "memory": self.memory,

            "recommendation": self.recommendation,

            "created_at": self.created_at,
        }