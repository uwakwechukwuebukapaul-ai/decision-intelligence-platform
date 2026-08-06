"""
Investigation Memory

Stores and retrieves previous
investigation intelligence.
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass
class InvestigationRecord:
    investigation_id: str
    data: dict[str, Any]
    created_at: str = field(
        default_factory=lambda:
       datetime.now(UTC).isoformat()
    )


class InvestigationMemory:
    """
    Memory storage for investigations.
    """

    def __init__(self):
        self.records: dict[str, InvestigationRecord] = {}


    def remember(
        self,
        investigation_id: str,
        data: dict[str, Any],
    ) -> InvestigationRecord:

        record = InvestigationRecord(
            investigation_id,
            data,
        )

        self.records[investigation_id] = record

        return record


    def recall(
        self,
        investigation_id: str,
    ) -> InvestigationRecord | None:

        return self.records.get(
            investigation_id
        )


    def count(self) -> int:

        return len(
            self.records
        )