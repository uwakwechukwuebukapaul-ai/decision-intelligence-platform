from flask import Blueprint, jsonify


from app.ai.autonomous_reasoning_engine.reasoning_controller import (
    ReasoningController
)



autonomous_reasoning_engine_bp = Blueprint(

    "autonomous_reasoning_engine",

    __name__

)



controller = ReasoningController()



@autonomous_reasoning_engine_bp.route(

    "/autonomous-reasoning-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_reasoning_engine(user_id):


    result = controller.generate_reasoning(

        user_id

    )


    return jsonify(

        {

            "status":

                "operational",


            "autonomous_reasoning_engine":

                result

        }

    )