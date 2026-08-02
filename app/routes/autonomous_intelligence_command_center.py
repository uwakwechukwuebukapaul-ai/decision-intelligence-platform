from flask import Blueprint, jsonify

from app.ai.autonomous_intelligence_command_center import (
    CommandController
)


autonomous_intelligence_command_center = Blueprint(
    "autonomous_intelligence_command_center",
    __name__
)


@autonomous_intelligence_command_center.route(
    "/autonomous-intelligence-command-center/<int:user_id>",
    methods=["GET"]
)
def autonomous_intelligence_command_center_route(user_id):

    controller = CommandController(
        user_id
    )

    result = controller.execute_command_cycle()


    return jsonify({

        "status":
            "operational",

        "user_id":
            user_id,

        "autonomous_intelligence_command_center":
            result

    })