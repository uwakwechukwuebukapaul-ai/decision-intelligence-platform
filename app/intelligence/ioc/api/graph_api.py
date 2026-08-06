"""
Sentinel DNA

IOC Graph API Service

Provides intelligence graph responses.
"""

from __future__ import annotations


from app.intelligence.ioc.graph import (
    EntityGraph,
    RelationshipEngine,
)



class IOCGraphAPI:
    """
    Builds IOC intelligence graph responses.
    """



    def __init__(self):

        self.graph = EntityGraph()

        self.relationship_engine = RelationshipEngine()



    def build_graph(
        self,
        indicator: str,
        indicator_type: str,
    ) -> dict:
        """
        Build intelligence graph.
        """


        root = self.graph.add_entity(
            entity_id=indicator,
            entity_type=indicator_type,
            metadata={
                "source": "ioc-service"
            },
        )


        relationships = []


        return {

            "indicator": indicator,

            "entity": root,

            "relationships": relationships,

            "graph_status": "generated",

        }