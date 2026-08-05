from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class EngineMessage:
    """
    Universal communication format
    used by Sentinel DNA engines.
    """

    source: str
    event: str
    severity: str = "LOW"
    payload: Dict[str, Any] = field(default_factory=dict)

    timestamp: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )

    correlation_id: str = ""

    def to_dict(self):

        return {
            "source": self.source,
            "event": self.event,
            "severity": self.severity,
            "payload": self.payload,
            "timestamp": self.timestamp,
            "correlation_id": self.correlation_id
        }