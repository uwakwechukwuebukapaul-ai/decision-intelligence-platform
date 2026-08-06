"""
Sentinel DNA Investigation Graph Engine
"""


from .graph_store import GraphStore

from .graph_schema import (
    GraphEntity,
    GraphRelationship,
)



class GraphEngine:


    def __init__(self):

        self.store = GraphStore()



    def register_indicator(
        self,
        intelligence: dict,
    ):


        indicator = intelligence.get(
            "indicator"
        )


        entity = GraphEntity(

            entity_id=indicator,

            entity_type="ioc",

            attributes=intelligence,

        )


        self.store.add_entity(
            entity
        )


        return entity



    def connect(
        self,
        source: str,
        relationship: str,
        target: str,
        confidence: int = 50,
    ):


        relation = GraphRelationship(

            source=source,

            relationship=relationship,

            target=target,

            confidence=confidence,

        )


        self.store.add_relationship(
            relation
        )


        return relation



    def ingest_intelligence(
        self,
        intelligence: dict,
    ):


        entity = self.register_indicator(
            intelligence
        )


        for relation in intelligence.get(
            "relationships",
            []
        ):


            self.connect(

                relation.get(
                    "source"
                ),

                relation.get(
                    "relationship"
                ),

                relation.get(
                    "target"
                ),

                relation.get(
                    "confidence",
                    0
                ),

            )


        return {

            "entity": entity.entity_id,

            "relationships": len(
                self.store.relationships
            )

        }