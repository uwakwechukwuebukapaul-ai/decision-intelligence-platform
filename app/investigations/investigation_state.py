"""
Sentinel DNA - Investigation State

Central investigation lifecycle state management.

Provides:

- InvestigationStatus
- AgentStatus
- InvestigationState
"""

from __future__ import annotations

from datetime import datetime, UTC
from enum import Enum
from typing import Dict, Any, List


class InvestigationStatus(str, Enum):
    """
    Investigation lifecycle states.
    """

    CREATED = "CREATED"
    RUNNING = "RUNNING"
    ANALYZING = "ANALYZING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class AgentStatus(str, Enum):
    """
    AI agent execution states.
    """

    IDLE = "IDLE"
    RUNNING = "RUNNING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class InvestigationState:
    """
    Runtime state container
    for AI SOC investigations.
    """

    def __init__(
        self,
        investigation_id: str,
    ):

        self.investigation_id = investigation_id

        self.status = InvestigationStatus.CREATED

        self.created_at = datetime.now(UTC)

        self.updated_at = datetime.now(UTC)

        self.agents: Dict[str, Dict[str, Any]] = {}

        self.timeline: List[Dict[str, Any]] = []

        self.findings: List[Dict[str, Any]] = []

        self.results: Dict[str, Any] = {}

        self.risk_score: int = 0

        self.confidence_score: float = 0.0

        self.classification: str | None = None

        self.recommendations: List[str] = []


    # =====================================================
    # Lifecycle Management
    # =====================================================

    def update_status(
        self,
        status: InvestigationStatus,
    ):

        self.status = status

        self.updated_at = datetime.now(UTC)


    def start(self):

        self.status = InvestigationStatus.RUNNING

        self.add_event(
            "Investigation started"
        )


    def analyze(self):

        self.status = InvestigationStatus.ANALYZING

        self.add_event(
            "Investigation analysis started"
        )


    def complete(self):

        self.status = InvestigationStatus.COMPLETED

        self.add_event(
            "Investigation completed"
        )


    def fail(
        self,
        reason: str | None = None,
    ):

        self.status = InvestigationStatus.FAILED

        self.add_event(
            "Investigation failed",
            {
                "reason": reason
            }
        )


    # =====================================================
    # AI Agent Management
    # =====================================================

    def register_agent(
        self,
        agent_name: str,
    ):

        self.agents[agent_name] = {

            "status":
                AgentStatus.RUNNING.value,

            "started":
                datetime.now(UTC).isoformat(),

            "completed":
                None,
        }

        self.updated_at = datetime.now(UTC)


    def update_agent(
        self,
        agent_name: str,
        status: AgentStatus | str,
        metadata: dict | None = None,
    ):

        if agent_name not in self.agents:

            self.register_agent(agent_name)


        if isinstance(status, AgentStatus):

            status = status.value


        self.agents[agent_name]["status"] = status


        if metadata:

            self.agents[agent_name].update(
                metadata
            )


        self.updated_at = datetime.now(UTC)


    def complete_agent(
        self,
        agent_name: str,
    ):

        self.update_agent(
            agent_name,
            AgentStatus.COMPLETED,
            {
                "completed":
                    datetime.now(UTC).isoformat()
            }
        )


    def fail_agent(
        self,
        agent_name: str,
    ):

        self.update_agent(
            agent_name,
            AgentStatus.FAILED
        )


    # =====================================================
    # Intelligence Data
    # =====================================================

    def add_finding(
        self,
        finding: Dict[str, Any],
    ):

        self.findings.append(
            {
                "finding": finding,

                "timestamp":
                    datetime.now(UTC).isoformat(),
            }
        )

        self.updated_at = datetime.now(UTC)


    def add_result(
        self,
        agent_name: str,
        result: Dict[str, Any],
    ):

        self.results[agent_name] = {

            "result": result,

            "timestamp":
                datetime.now(UTC).isoformat(),
        }

        self.updated_at = datetime.now(UTC)


    def set_risk_score(
        self,
        score: int,
    ):

        self.risk_score = score

        self.add_event(
            "Risk score updated",
            {
                "score": score
            }
        )


    def set_confidence_score(
        self,
        score: float,
    ):

        self.confidence_score = score

        self.updated_at = datetime.now(UTC)


    def set_classification(
        self,
        classification: str,
    ):

        self.classification = classification

        self.updated_at = datetime.now(UTC)


    def add_recommendation(
        self,
        recommendation: str,
    ):

        self.recommendations.append(
            recommendation
        )

        self.updated_at = datetime.now(UTC)


    # =====================================================
    # Timeline / Audit
    # =====================================================

    def add_event(
        self,
        event: str,
        metadata: dict | None = None,
    ):

        self.timeline.append(
            {
                "event": event,

                "metadata": metadata or {},

                "timestamp":
                    datetime.now(UTC).isoformat(),
            }
        )

        self.updated_at = datetime.now(UTC)


    # =====================================================
    # Reporting Helpers
    # =====================================================

    def get_summary(self):

        return {

            "investigation_id":
                self.investigation_id,

            "status":
                self.status.value,

            "risk_score":
                self.risk_score,

            "confidence_score":
                self.confidence_score,

            "classification":
                self.classification,

            "findings_count":
                len(self.findings),

            "agents_count":
                len(self.agents),

            "timeline_events":
                len(self.timeline),
        }


    # =====================================================
    # Serialization
    # =====================================================

    def to_dict(self):

        return {

            "investigation_id":
                self.investigation_id,

            "status":
                self.status.value,

            "created_at":
                self.created_at.isoformat(),

            "updated_at":
                self.updated_at.isoformat(),

            "agents":
                self.agents,

            "findings":
                self.findings,

            "results":
                self.results,

            "risk_score":
                self.risk_score,

            "confidence_score":
                self.confidence_score,

            "classification":
                self.classification,

            "recommendations":
                self.recommendations,

            "timeline":
                self.timeline,
        }