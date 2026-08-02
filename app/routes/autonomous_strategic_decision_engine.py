from flask import Blueprint, jsonify

from app.ai.autonomous_strategic_decision_engine import (
    StrategicController
)


autonomous_strategic_decision_engine = Blueprint(
    "autonomous_strategic_decision_engine",
    __name__
)



@autonomous_strategic_decision_engine.route(
    "/autonomous-strategic-decision-engine/<int:user_id>",
    methods=["GET"]
)
def autonomous_strategic_decision(user_id):


    controller = StrategicController(
        user_id
    )


    result = controller.execute_strategic_cycle()


    return jsonify({

        "status":
            "operational",

        "user_id":
            user_id,

        "strategic_decision_engine":
            result

    })