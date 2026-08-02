from flask import Blueprint, jsonify

from app.ai.autonomous_intelligence_fusion_engine import (
    FusionController
)


autonomous_intelligence_fusion_engine = Blueprint(

    "autonomous_intelligence_fusion_engine",

    __name__

)



@autonomous_intelligence_fusion_engine.route(
    "/autonomous-intelligence-fusion-engine/<int:user_id>",
    methods=["GET"]
)

def autonomous_intelligence_fusion(user_id):


    controller = FusionController(
        user_id
    )


    result = controller.execute_fusion_cycle()


    return jsonify({

        "status":
            "operational",

        "user_id":
            user_id,

        "fusion_intelligence":
            result

    })