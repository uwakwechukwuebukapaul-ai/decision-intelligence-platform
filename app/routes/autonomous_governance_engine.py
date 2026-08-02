from flask import Blueprint, jsonify

from app.ai.autonomous_governance_engine import (
    GovernanceController
)


autonomous_governance_engine = Blueprint(

    "autonomous_governance_engine",

    __name__

)



@autonomous_governance_engine.route(

    "/autonomous-governance-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_governance(user_id):


    controller = GovernanceController(user_id)


    result = controller.execute_governance_cycle()


    return jsonify({

        "status":
            "operational",

        "user_id":
            user_id,

        "autonomous_governance_engine":
            result

    })