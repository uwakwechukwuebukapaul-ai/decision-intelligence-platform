"""
Sentinel DNA Graph Store

Temporary in-memory graph storage layer.

Designed for future migration to:
- Neo4j
- PostgreSQL graph extension
- Graph databases
"""


from typing import Dict, List

from .graph_schema import (
    GraphEntity,
    GraphRelationship,
)



class GraphStore:


    def __init__(self):

        self.entities: Dict[str, GraphEntity] = {}

        self.relationships: List[
            GraphRelationship
        ] = []



    def add_entity(
        self,
        entity: GraphEntity,
    ):

        self.entities[
            entity.entity_id
        ] = entity


        return entity



    def add_relationship(
        self,
        relationship: GraphRelationship,
    ):

        self.relationships.append(
            relationship
        )


        return relationship



    def get_entity(
        self,
        entity_id: str,
    ):

        return self.entities.get(
            entity_id
        )



    def get_relationships(
        self,
        entity_id: str,
    ):

        return [

            relation

            for relation in self.relationships

            if relation.source == entity_id
            or relation.target == entity_id

        ]