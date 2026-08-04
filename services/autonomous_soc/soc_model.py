from dataclasses import dataclass, field
from typing import List, Dict, Any


@dataclass
class SOCWorkflowModel:
    """
    Autonomous SOC workflow state model.

    Represents the lifecycle of an AI SOC investigation:

    Alert
      |
    Planning
      |
    Investigation
      |
    Analyst Reasoning
      |
    Decision
      |
    Response
    """

    event: str

    investigation_plan: List[str] = field(
        default_factory=list
    )

    analyst_findings: List[str] = field(
        default_factory=list
    )

    decisions: List[Dict[str, Any]] = field(
        default_factory=list
    )

    confidence: float = 0.0

    status: str = "initialized"


    def add_finding(
        self,
        finding: str
    ):

        self.analyst_findings.append(
            finding
        )


    def add_decision(
        self,
        decision: Dict[str, Any]
    ):

        self.decisions.append(
            decision
        )


    def complete(
        self
    ):

        self.status = "completed"


    def to_dict(
        self
    ):

        return {

            "event":
                self.event,

            "investigation_plan":
                self.investigation_plan,

            "analyst_findings":
                self.analyst_findings,

            "decisions":
                self.decisions,

            "confidence":
                self.confidence,

            "status":
                self.status

        }