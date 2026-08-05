"""
Decision Intelligence Platform

Intelligence Execution API

Provides a unified execution gateway
for registered intelligence capabilities.
"""

from flask import (
    Blueprint,
    request,
    jsonify
)


from app.intelligence.capability_registry import (
    capability_registry
)


intelligence_execution_bp = Blueprint(
    "intelligence_execution",
    __name__
)


@intelligence_execution_bp.route(
    "/intelligence/execute",
    methods=["POST"]
)
def execute_intelligence():

    payload = request.get_json() or {}


    user_id = payload.get(
        "user_id"
    )

    capability = payload.get(
        "capability"
    )

    objective = payload.get(
        "objective"
    )


    if not capability:

        return jsonify({

            "status":
                "error",

            "message":
                "Capability is required"

        }), 400



    if not capability_registry.has_capability(
        capability
    ):

        return jsonify({

            "status":
                "error",

            "message":
                "Unknown capability",

            "capability":
                capability

        }), 404



    result = capability_registry.execute(

        capability,

        {

            "user_id":
                user_id,

            "objective":
                objective

        }

    )


    return jsonify({

        "status":
            "success",

        "capability":
            capability,

        "user_id":
            user_id,

        "objective":
            objective,

        "result":
            result

    }), 200