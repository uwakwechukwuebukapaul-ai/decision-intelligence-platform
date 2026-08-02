from flask import Blueprint, jsonify


from app.ai.knowledge_graph_engine.knowledge_graph import (
    knowledge_graph_engine
)



intelligence_knowledge_graph_bp = Blueprint(

    "intelligence_knowledge_graph",

    __name__

)



@intelligence_knowledge_graph_bp.route(

    "/intelligence-knowledge-graph/<int:user_id>",

    methods=["GET"]

)

def intelligence_knowledge_graph(user_id):


    result = knowledge_graph_engine.generate_graph(

        user_id

    )


    return jsonify({

        "knowledge_graph_engine":

            result

    })