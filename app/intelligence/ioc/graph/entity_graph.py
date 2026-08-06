"""
Sentinel DNA

IOC Entity Graph

Core internal representation of security entities.

Future expansion:
- Graph database integration
- Neo4j support
- Threat actor relationship mapping
"""


from __future__ import annotations


class EntityGraph:
    """
    In-memory intelligence graph.

    Stores relationships between
    security entities.
    """


    def __init__(self):

        self.entities = {}

        self.relationships = []



    def add_entity(
        self,
        entity_id: str,
        entity_type: str,
        metadata: dict | None = None,
    ) -> dict:
        """
        Add entity to graph.
        """


        entity = {

            "id": entity_id,

            "type": entity_type,

            "metadata": metadata or {},

        }


        self.entities[entity_id] = entity


        return entity



    def add_relationship(
        self,
        source: str,
        target: str,
        relationship_type: str,
    ) -> dict:
        """
        Connect entities.
        """


        relationship = {

            "source": source,

            "target": target,

            "type": relationship_type,

        }


        self.relationships.append(
            relationship
        )


        return relationship



    def get_entity(
        self,
        entity_id: str,
    ) -> dict | None:

        return self.entities.get(
            entity_id
        )



    def get_relationships(
        self,
    ) -> list:

        return self.relationships