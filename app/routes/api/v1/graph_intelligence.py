"""
Sentinel DNA - Graph Intelligence API

Exposes investigation knowledge graph capabilities.
"""

from flask import Blueprint, jsonify

from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)

from app.intelligence.graph import (
    GraphEngine,
    GraphQuery,
)



graph_intelligence_api_bp = Blueprint(
    "graph_intelligence_api",
    __name__,
)



@graph_intelligence_api_bp.route(
    "/api/v1/graph/ioc/<indicator>",
    methods=["GET"],
)
def get_ioc_graph(indicator):


    try:

        intelligence = (
            IntelligenceFusion()
            .analyze(indicator)
        )


        graph = GraphEngine()


        graph.ingest_intelligence(
            intelligence
        )


        query = GraphQuery(
            graph.store
        )


        result = query.investigate_entity(
            indicator
        )


        relationships = []


        for relation in result[
            "relationships"
        ]:


            relationships.append(

                {

                    "relationship":
                        relation.relationship,


                    "target":
                        relation.target,


                    "confidence":
                        relation.confidence,

                }

            )


        return jsonify(

            {

                "service":
                    "graph-intelligence",


                "indicator":
                    indicator,


                "entity_type":
                    "ioc",


                "relationship_count":
                    len(
                        relationships
                    ),


                "connections":
                    relationships,

            }

        )


    except Exception as exc:


        return jsonify(

            {

                "service":
                    "graph-intelligence",


                "status":
                    "failed",


                "error":
                    str(exc),

            }

        ), 500