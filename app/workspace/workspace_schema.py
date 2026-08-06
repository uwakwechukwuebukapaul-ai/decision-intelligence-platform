"""
Sentinel DNA - Workspace Schemas

Data models for analyst operations.
"""


from __future__ import annotations


from dataclasses import dataclass, field
from datetime import datetime





@dataclass
class WorkspaceIncident:
    """
    Analyst-facing incident representation.
    """


    incident_id: str

    indicator: str

    severity: str = "medium"

    status: str = "open"

    assigned_to: str | None = None

    timeline: list = field(
        default_factory=list
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )


    def to_dict(self):

        return {

            "incident_id":
                self.incident_id,

            "indicator":
                self.indicator,

            "severity":
                self.severity,

            "status":
                self.status,

            "assigned_to":
                self.assigned_to,

            "timeline":
                self.timeline,

            "created_at":
                self.created_at,

        }