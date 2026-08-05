from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class GraphEntity:
    """
    Represents an intelligence entity.

    Examples:

    - Threat actor
    - Malware
    - IOC
    - Vulnerability
    - Host
    - Technique
    - Incident
    """

    name: str

    entity_type: str

    attributes: Dict = field(
        default_factory=dict
    )



@dataclass
class GraphRelationship:
    """
    Represents relationships between entities.
    """

    source: str

    target: str

    relationship: str

    confidence: float = 1.0



class KnowledgeGraph:
    """
    Core Sentinel DNA intelligence graph.

    Stores:

    Entities
    Relationships
    """

    def __init__(self):

        self.entities = {}

        self.relationships = []



    def add_entity(
        self,
        entity: GraphEntity
    ):

        self.entities[
            entity.name
        ] = entity



    def add_relationship(
        self,
        relationship: GraphRelationship
    ):

        self.relationships.append(
            relationship
        )



    def get_entity(
        self,
        name
    ):

        return self.entities.get(
            name
        )



    def find_relationships(
        self,
        entity
    ):

        return [

            r for r in self.relationships

            if r.source == entity
            or r.target == entity

        ]



    def export(self):

        return {

            "entities":
                [
                    entity.__dict__

                    for entity in self.entities.values()

                ],


            "relationships":
                [

                    relationship.__dict__

                    for relationship in self.relationships

                ]

        }