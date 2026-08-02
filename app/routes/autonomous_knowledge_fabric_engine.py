from flask import Blueprint, jsonify


from app.ai.autonomous_knowledge_fabric_engine import (
    KnowledgeController
)



autonomous_knowledge_fabric_engine = Blueprint(

    "autonomous_knowledge_fabric_engine",

    __name__

)



controller = KnowledgeController()



@autonomous_knowledge_fabric_engine.route(

    "/autonomous-knowledge-fabric-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_knowledge_fabric(user_id):


    result = controller.execute_knowledge_cycle(

        user_id

    )


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_knowledge_fabric_engine":

            result

    })