"""
Sentinel DNA

Investigation Playbook
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class Playbook:
    """
    Represents an investigation playbook.
    """

    name: str

    description: str = ""

    stages: list[str] = field(default_factory=list)

    enabled: bool = True

    metadata: dict = field(default_factory=dict)

    def add_stage(
        self,
        stage: str,
    ) -> None:

        self.stages.append(stage)

    def remove_stage(
        self,
        stage: str,
    ) -> None:

        if stage in self.stages:
            self.stages.remove(stage)

    def enable(self) -> None:

        self.enabled = True

    def disable(self) -> None:

        self.enabled = False

    def to_dict(self) -> dict:

        return {

            "name": self.name,

            "description": self.description,

            "stages": list(self.stages),

            "enabled": self.enabled,

            "metadata": dict(self.metadata),

        }