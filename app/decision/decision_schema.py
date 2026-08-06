"""
Sentinel DNA Decision Schema

Defines AI decision output structure.
"""


from dataclasses import dataclass, asdict
from datetime import datetime



@dataclass
class DecisionSchema:

    incident_id: str

    decision: str

    priority: str

    confidence: float

    actions: list

    reasoning: list

    created_at: str = None


    def __post_init__(self):

        if self.created_at is None:
            self.created_at = datetime.utcnow().isoformat()



    def to_dict(self):

        return asdict(self)