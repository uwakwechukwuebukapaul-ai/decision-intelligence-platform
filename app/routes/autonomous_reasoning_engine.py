from flask import Blueprint, jsonify


from app.ai.autonomous_reasoning_engine.reasoning_controller import (
    ReasoningController
)



# =====================================================
# Blueprint Definition
# =====================================================

autonomous_reasoning_engine = Blueprint(

    "autonomous_reasoning_engine",

    __name__

)



# =====================================================
# Controller
# =====================================================

controller = ReasoningController()



# =====================================================
# Autonomous Reasoning Endpoint
# =====================================================

@autonomous_reasoning_engine.route(

    "/autonomous-reasoning-engine/<int:user_id>",

    methods=["GET"]

)

def get_autonomous_reasoning_engine(user_id):


    result = controller.generate_reasoning(

        user_id

    )


    return jsonify(

        {

            "status":

                "operational",


            "user_id":

                user_id,


            "autonomous_reasoning_engine":

                result

        }

    )