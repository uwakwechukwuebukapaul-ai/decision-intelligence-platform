"""
Decision Intelligence Platform

Health and Platform Status Routes
"""

from flask import Blueprint, jsonify
from datetime import datetime


health_bp = Blueprint(
    "health",
    __name__
)


@health_bp.route(
    "/health",
    methods=["GET"]
)
def health():

    return jsonify({

        "platform":
            "Decision Intelligence Platform",

        "status":
            "healthy",

        "version":
            "49.0",

        "services": {

            "database":
                "active",

            "intelligence_fabric":
                "active",

            "capability_registry":
                "active",

            "autonomous_stack":
                "active",

            "agent_runtime":
                "active",

            "control_plane":
                "active"

        },

        "timestamp":
            datetime.utcnow().isoformat()

    })


@health_bp.route(
    "/intelligence-status",
    methods=["GET"]
)
def intelligence_status():

    from app.intelligence.capability_registry import (
        capability_registry
    )

    return jsonify({

        "platform":
            "Decision Intelligence Platform",

        "version":
            "49.0",

        "registered_capabilities":
            capability_registry.list_capabilities(),

        "timestamp":
            datetime.utcnow().isoformat()

    })