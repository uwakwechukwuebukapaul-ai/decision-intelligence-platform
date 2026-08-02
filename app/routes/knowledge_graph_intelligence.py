from flask import Blueprint, jsonify

from app.ai.knowledge_graph_intelligence.graph_controller import (
    GraphController
)



knowledge_graph_intelligence_bp = Blueprint(

    "knowledge_graph_intelligence",

    __name__

)



controller = GraphController()



@knowledge_graph_intelligence_bp.route(
    "/knowledge-graph-intelligence/<int:user_id>",
    methods=["GET"]
)

def knowledge_graph_intelligence(user_id):


    result = controller.generate_graph_intelligence(

        user_id

    )


    return jsonify(

        {

            "status":
                "operational",

            "knowledge_graph_intelligence":
                result

        }

    )