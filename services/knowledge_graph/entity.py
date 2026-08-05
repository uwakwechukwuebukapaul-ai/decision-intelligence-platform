from dataclasses import dataclass, field
from typing import Dict


@dataclass
class Entity:
    """
    Represents an intelligence entity.
    """

    name: str
    entity_type: str
    attributes: Dict = field(default_factory=dict)

    def to_dict(self):

        return {
            "name": self.name,
            "type": self.entity_type,
            "attributes": self.attributes
        }