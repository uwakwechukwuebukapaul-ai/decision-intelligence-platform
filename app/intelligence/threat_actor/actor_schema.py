"""
Sentinel DNA - Threat Actor Schemas
"""


from dataclasses import dataclass, field

from datetime import datetime

from typing import List, Dict, Any






@dataclass
class ThreatActorResult:
    """
    Threat actor intelligence result.
    """


    indicator: str

    actor_match: bool

    confidence: int

    actors: List[Dict[str, Any]] = field(
        default_factory=list
    )


    reasoning: List[str] = field(
        default_factory=list
    )


    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )



    def to_dict(self):

        return {

            "indicator":
            self.indicator,


            "actor_match":
            self.actor_match,


            "confidence":
            self.confidence,


            "actors":
            self.actors,


            "reasoning":
            self.reasoning,


            "created_at":
            self.created_at,
        }