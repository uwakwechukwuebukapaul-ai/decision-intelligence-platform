"""
Sentinel DNA Knowledge Graph Intelligence Core.

Provides:

- Entity extraction
- Relationship mapping
- Knowledge graph storage
- Attack graph reasoning
- Sentinel Core integration
"""


from .graph_model import (
    GraphEntity,
    GraphRelationship,
    KnowledgeGraph
)


from .entity_engine import EntityEngine

from .relationship_engine import RelationshipEngine

from .attack_graph import AttackGraphEngine



class KnowledgeGraphEngine:
    """
    High level Knowledge Graph service interface.

    Compatible with Sentinel Core pipeline.
    """


    def __init__(self):

        self.graph = KnowledgeGraph()

        self.entity_engine = EntityEngine()

        self.relationship_engine = RelationshipEngine()

        self.attack_graph_engine = AttackGraphEngine()



    def analyze(
        self,
        text
    ):

        entities = self.entity_engine.extract(
            text
        )


        for entity in entities:

            self.graph.add_entity(
                entity
            )


        relationships = self.relationship_engine.build(
            entities
        )


        for relationship in relationships:

            self.graph.add_relationship(
                relationship
            )


        attack_graph = self.attack_graph_engine.build_attack_path(
            entities,
            relationships
        )


        return {

            "entities":
                [
                    entity.__dict__

                    for entity in entities
                ],


            "relationships":
                [
                    relationship.__dict__

                    for relationship in relationships
                ],


            "attack_graph":
                attack_graph,


            "status":
                "knowledge_graph_processed"

        }



    def process(
        self,
        event
    ):
        """
        Backward compatible Sentinel Core API.

        Sentinel pipeline calls:
        
        graph.process(event)
        """

        return self.analyze(
            event
        )



__all__ = [

    "GraphEntity",

    "GraphRelationship",

    "KnowledgeGraph",

    "KnowledgeGraphEngine",

    "EntityEngine",

    "RelationshipEngine",

    "AttackGraphEngine"

]