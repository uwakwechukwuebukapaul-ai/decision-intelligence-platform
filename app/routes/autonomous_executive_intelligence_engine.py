from flask import Blueprint, jsonify


from app.ai.autonomous_executive_intelligence_engine import (
    ExecutiveController
)



autonomous_executive_intelligence_engine = Blueprint(
    "autonomous_executive_intelligence_engine",
    __name__
)



@autonomous_executive_intelligence_engine.route(
    "/autonomous-executive-intelligence-engine/<int:user_id>",
    methods=["GET"]
)
def autonomous_executive_intelligence(user_id):


    controller = ExecutiveController(
        user_id
    )


    result = controller.execute_executive_cycle()


    return jsonify({

        "status":
            "operational",

        "user_id":
            user_id,

        "executive_intelligence_engine":
            result

    })