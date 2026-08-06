"""
Sentinel DNA

Pipeline Context

Shared investigation context used across the
entire execution pipeline.
"""

from __future__ import annotations

from datetime import UTC, datetime
import uuid


class PipelineContext:
    """
    Shared execution context.

    Travels through every investigation stage.
    """

    def __init__(
        self,
        capability: str,
        payload: dict | None = None,
    ) -> None:

        self.investigation_id = str(uuid.uuid4())

        self.capability = capability

        self.payload = payload or {}

        self.metadata: dict = {}

        self.evidence: list = []

        self.findings: list = []

        self.completed_stages: list = []

        self.created_at = datetime.now(
            UTC
        ).isoformat()

    def add_metadata(
        self,
        key: str,
        value,
    ) -> None:

        self.metadata[key] = value

    def get_metadata(
        self,
        key: str,
        default=None,
    ):

        return self.metadata.get(
            key,
            default,
        )

    def add_evidence(
        self,
        evidence,
    ) -> None:

        self.evidence.append(
            evidence,
        )

    def add_finding(
        self,
        finding,
    ) -> None:

        self.findings.append(
            finding,
        )

    def complete_stage(
        self,
        stage: str,
    ) -> None:

        self.completed_stages.append(
            stage,
        )

    def to_dict(self) -> dict:

        return {

            "investigation_id": self.investigation_id,

            "capability": self.capability,

            "payload": self.payload,

            "metadata": self.metadata,

            "evidence": self.evidence,

            "findings": self.findings,

            "completed_stages": self.completed_stages,

            "created_at": self.created_at,
        }