"""
Sentinel DNA API Gateway v1

Intelligence API

External-facing intelligence endpoints.
"""

from flask import (
    Blueprint,
    jsonify,
)


intelligence_api_bp = Blueprint(
    "intelligence_api",
    __name__,
    url_prefix="/api/v1/intelligence",
)


@intelligence_api_bp.route(
    "/health",
    methods=["GET"],
)
def intelligence_health():

    return jsonify(
        {
            "service": "intelligence-api",
            "status": "healthy",
            "version": "v1",
        }
    )