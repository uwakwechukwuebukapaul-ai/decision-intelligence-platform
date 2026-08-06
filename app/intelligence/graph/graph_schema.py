"""
Sentinel DNA Graph Schema

Defines entities and relationships.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any



@dataclass
class GraphEntity:

    entity_id: str

    entity_type: str

    attributes: Dict[str, Any] = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )



@dataclass
class GraphRelationship:

    source: str

    relationship: str

    target: str

    confidence: int = 0

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    created_at: str = field(
        default_factory=lambda:
        datetime.utcnow().isoformat()
    )