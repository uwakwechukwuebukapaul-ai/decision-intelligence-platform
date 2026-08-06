"""
Agent Memory

Stores agent experiences,
actions and outcomes.
"""

from dataclasses import dataclass, field
from datetime import datetime, UTC
from typing import Any


@dataclass
class AgentExperience:
    """
    Represents an agent action and outcome.
    """

    agent_name: str
    action: str
    outcome: dict[str, Any]

    timestamp: str = field(
        default_factory=lambda:
        datetime.now(UTC).isoformat()
    )


class AgentMemory:
    """
    Stores intelligence agent experiences.
    """

    def __init__(self):

        self.experiences: list[AgentExperience] = []


    def remember(
        self,
        agent_name: str,
        action: str,
        outcome: dict[str, Any],
    ) -> AgentExperience:

        experience = AgentExperience(
            agent_name,
            action,
            outcome,
        )

        self.experiences.append(
            experience
        )

        return experience


    def history(
        self,
        agent_name: str | None = None,
    ) -> list[AgentExperience]:

        if agent_name is None:
            return self.experiences


        return [
            item
            for item in self.experiences
            if item.agent_name == agent_name
        ]


    def count(self) -> int:

        return len(
            self.experiences
        )