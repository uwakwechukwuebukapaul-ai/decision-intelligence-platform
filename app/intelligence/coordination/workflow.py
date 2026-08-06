"""
Workflow Models

Defines investigation workflows and
their ordered execution steps.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class WorkflowStep:
    """
    A single workflow step.
    """

    name: str
    capability: str
    payload: dict[str, Any] = field(default_factory=dict)
    depends_on: list[str] = field(default_factory=list)


@dataclass(slots=True)
class Workflow:
    """
    Investigation workflow definition.
    """

    name: str
    description: str
    steps: list[WorkflowStep] = field(default_factory=list)

    def add_step(
        self,
        step: WorkflowStep,
    ) -> None:
        self.steps.append(step)

    def step_names(self) -> list[str]:
        return [
            step.name
            for step in self.steps
        ]

    def step_count(self) -> int:
        return len(self.steps)

    def to_dict(self) -> dict:

        return {
            "name": self.name,
            "description": self.description,
            "steps": [
                {
                    "name": step.name,
                    "capability": step.capability,
                    "payload": step.payload,
                    "depends_on": step.depends_on,
                }
                for step in self.steps
            ],
        }