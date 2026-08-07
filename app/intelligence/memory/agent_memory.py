"""
Agent Memory

Stores agent experiences,
actions and outcomes.
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime
from typing import Any


@dataclass(slots=True)
class AgentExperience:
    """
    Represents an agent action and outcome.
    """

    agent_name: str
    action: str
    outcome: dict[str, Any]

    timestamp: str = field(
        default_factory=lambda: datetime.now(UTC).isoformat()
    )


class AgentMemory:
    """
    Stores intelligence agent experiences.
    """

    def __init__(self) -> None:

        self.experiences: list[AgentExperience] = []

    def remember(
        self,
        agent_name: str,
        action: str,
        outcome: dict[str, Any],
    ) -> AgentExperience:
        """
        Store an agent experience.
        """

        experience = AgentExperience(
            agent_name=agent_name,
            action=action,
            outcome=outcome,
        )

        self.experiences.append(experience)

        return experience

    def history(
        self,
        agent_name: str | None = None,
    ) -> list[AgentExperience]:
        """
        Return stored experiences.
        """

        if agent_name is None:
            return list(self.experiences)

        return [
            experience
            for experience in self.experiences
            if experience.agent_name == agent_name
        ]

    def count(self) -> int:
        """
        Return total number of experiences.
        """

        return len(self.experiences)

    def clear(self) -> None:
        """
        Remove all stored experiences.
        """

        self.experiences.clear()