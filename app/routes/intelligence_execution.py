"""
Decision Intelligence Platform

Intelligence Execution API

Provides a unified execution gateway
for registered intelligence capabilities.

Enterprise responsibilities:
- Request validation
- Governance enforcement
- Policy evaluation
- Capability execution
- Runtime health tracking
"""

from flask import (
    Blueprint,
    request,
    jsonify
)


from app.intelligence.capability_registry import (
    capability_registry
)


from app.intelligence.governance.governance_middleware import (
    governance_middleware
)


from app.intelligence.governance.capability_health import (
    capability_health_manager
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


    # =====================================
    # Validation
    # =====================================

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



    # =====================================
    # Governance Enforcement
    # =====================================

    governance_result = (
        governance_middleware.evaluate(
            capability=capability,
            user_id=user_id,
            objective=objective
        )
    )


    if not governance_result.get(
        "allowed",
        False
    ):

        return jsonify({

            "status":
                "blocked",

            "capability":
                capability,

            "governance":
                governance_result

        }), 403



    # =====================================
    # Execute Capability
    # =====================================

    try:

        result = capability_registry.execute(

            capability,

            {

                "user_id":
                    user_id,

                "objective":
                    objective

            }

        )


        capability_health_manager.record_success(
            capability
        )


    except Exception as error:


        capability_health_manager.record_failure(

            capability,

            str(error)

        )


        return jsonify({

            "status":
                "error",

            "message":
                str(error)

        }), 500



    # =====================================
    # Response
    # =====================================

    return jsonify({

        "status":
            "success",

        "capability":
            capability,

        "user_id":
            user_id,

        "objective":
            objective,

        "governance":
            governance_result,

        "result":
            result

    }), 200