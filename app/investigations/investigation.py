"""
Sentinel DNA Investigation Object

Represents a complete security investigation.
"""

from __future__ import annotations

from typing import Any, Dict, List

from app.core.time import utc_now

from .investigation_state import InvestigationState


class Investigation:
    """
    Core investigation container.

    Holds:
    - Case reference
    - Evidence
    - AI investigation state
    - Agent execution lifecycle
    """

    def __init__(
        self,
        investigation_id: str,
        case_id: str | None = None,
        evidence: List[Dict[str, Any]] | None = None,
    ):

        self.investigation_id = investigation_id

        self.case_id = case_id

        self.evidence = evidence or []

        self.state = InvestigationState(
            investigation_id
        )

        self.created_at = utc_now()

        self.updated_at = utc_now()


    # ==========================
    # Agent Management
    # ==========================

    def add_agent(
        self,
        agent_name: str,
    ):

        self.state.register_agent(
            agent_name
        )

        self.updated_at = utc_now()


    # ==========================
    # Lifecycle
    # ==========================

    def start(self):

        self.state.start()

        self.updated_at = utc_now()


    def complete(self):

        self.state.complete()

        self.updated_at = utc_now()


    # ==========================
    # Findings
    # ==========================

    def add_finding(
        self,
        finding: Dict[str, Any],
    ):

        self.state.add_finding(
            finding
        )

        self.updated_at = utc_now()


    # ==========================
    # Reporting
    # ==========================

    def report(self):

        return {

            "investigation_id":
                self.investigation_id,

            "case_id":
                self.case_id,

            "evidence_count":
                len(self.evidence),

            "created_at":
                self.created_at.isoformat(),

            "updated_at":
                self.updated_at.isoformat(),

            "state":
                self.state.to_dict(),

        }