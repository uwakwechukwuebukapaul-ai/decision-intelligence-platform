from flask import Blueprint, jsonify


from app.ai.autonomous_cognitive_intelligence_engine import (
    CognitiveController
)



autonomous_cognitive_intelligence_engine = Blueprint(

    "autonomous_cognitive_intelligence_engine",

    __name__

)



@autonomous_cognitive_intelligence_engine.route(

    "/autonomous-cognitive-intelligence-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_cognitive_intelligence(user_id):


    controller = CognitiveController(

        user_id

    )


    result = controller.execute_cognitive_cycle()


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_cognitive_intelligence_engine":

            result

    })