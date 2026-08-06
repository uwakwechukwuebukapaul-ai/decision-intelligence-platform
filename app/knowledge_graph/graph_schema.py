from dataclasses import dataclass
from datetime import datetime


@dataclass
class Entity:

    entity_id: str
    name: str
    entity_type: str
    created_at: str = datetime.utcnow().isoformat()



@dataclass
class Relationship:

    source: str
    target: str
    relationship: str
    confidence: float = 0.9
    created_at: str = datetime.utcnow().isoformat()