"""
Decision Intelligence Platform

Governance API Routes

Exposes governance decisions,
authorization checks,
and audit visibility.
"""


from flask import Blueprint, request, jsonify


from app.intelligence.governance.governance_middleware import (
    governance_middleware
)



governance_bp = Blueprint(

    "governance",

    __name__,

    url_prefix="/api/governance"

)



# =====================================
# Authorization Check
# =====================================


@governance_bp.route(
    "/authorize",
    methods=["POST"]
)
def authorize():


    payload = request.get_json() or {}


    capability = payload.get(
        "capability"
    )


    context = payload.get(
        "context",
        {}
    )


    if not capability:

        return jsonify({

            "error":
                "capability required"

        }), 400



    decision = governance_middleware.authorize(

        capability,

        context

    )


    return jsonify(

        decision.to_dict()

    )



# =====================================
# Audit Events
# =====================================


@governance_bp.route(
    "/audit",
    methods=["GET"]
)
def audit():


    return jsonify(

        governance_middleware.get_audit_events()

    )