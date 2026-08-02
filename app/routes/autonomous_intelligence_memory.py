from flask import Blueprint, jsonify

from app.ai.autonomous_intelligence_memory import (
    MemoryController
)


autonomous_intelligence_memory = Blueprint(
    "autonomous_intelligence_memory",
    __name__
)


@autonomous_intelligence_memory.route(
    "/autonomous-intelligence-memory/<int:user_id>",
    methods=["GET"]
)
def autonomous_intelligence_memory_route(user_id):

    controller = MemoryController(
        user_id
    )

    result = controller.generate_memory_state()


    return jsonify({

        "status":
            "operational",

        "user_id":
            user_id,

        "autonomous_intelligence_memory":
            result

    })