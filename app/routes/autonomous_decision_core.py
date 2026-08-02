from flask import Blueprint, jsonify


from app.ai.autonomous_decision_core.decision_controller import (
    generate_decision
)



autonomous_decision_core = Blueprint(

    "autonomous_decision_core",

    __name__

)



@autonomous_decision_core.route(

    "/autonomous-decision-core/<int:user_id>",

    methods=["GET"]

)

def get_autonomous_decision_core(user_id):


    result = generate_decision(user_id)


    return jsonify({

        "status":

            "operational",

        "user_id":

            user_id,

        "autonomous_decision_core":

            result

    })