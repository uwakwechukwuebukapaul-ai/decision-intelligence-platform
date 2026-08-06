"""
Investigation Strategy

Defines the reasoning plan
behind an intelligence investigation.
"""

from dataclasses import dataclass, field


@dataclass
class InvestigationStrategy:
    """
    Represents investigation intent.
    """

    objective: str

    capabilities: list[str] = field(
        default_factory=list
    )

    priority: str = "medium"


    def add_capability(
        self,
        capability: str,
    ) -> None:

        if capability not in self.capabilities:
            self.capabilities.append(
                capability
            )


    def to_dict(self) -> dict:

        return {
            "objective": self.objective,
            "capabilities": self.capabilities,
            "priority": self.priority,
        }