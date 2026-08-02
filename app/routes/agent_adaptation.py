from flask import Blueprint, jsonify


from app.ai.agent_adaptation.adaptation_engine import (
    AdaptationEngine
)



agent_adaptation_bp = Blueprint(

    "agent_adaptation",

    __name__

)



adaptation_engine = AdaptationEngine()



@agent_adaptation_bp.route(
    "/agent-adaptation/<int:user_id>",
    methods=["GET"]
)

def agent_adaptation(user_id):


    result = adaptation_engine.adapt(

        user_id

    )


    return jsonify({


        "agent_adaptation":

            result,


        "status":

            "operational"


    })