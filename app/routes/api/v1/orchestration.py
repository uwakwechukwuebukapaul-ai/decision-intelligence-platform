"""
Sentinel DNA - Investigation Orchestration API Gateway

Provides API access to autonomous investigation workflows.

Responsibilities:
- Accept IOC investigation requests
- Execute investigation orchestration
- Return analyst-ready intelligence
- Provide controlled API boundary
"""

from __future__ import annotations


import logging

from flask import Blueprint, jsonify


from app.autonomous_investigation.orchestration import (
    InvestigationOrchestrator,
)



logger = logging.getLogger(__name__)



orchestration_api_bp = Blueprint(
    "orchestration_api",
    __name__,
)



@orchestration_api_bp.route(
    "/api/v1/intelligence/ioc/<indicator>/orchestrate",
    methods=["GET"],
)
def orchestrate_investigation(
    indicator: str,
):
    """
    Execute autonomous investigation orchestration.

    Example:
    GET /api/v1/intelligence/ioc/example.xyz/orchestrate
    """

    try:

        orchestrator = InvestigationOrchestrator()


        result = orchestrator.execute(
            indicator
        )


        return jsonify(
            {
                "service":
                    "investigation-orchestration",

                "indicator":
                    indicator,

                "status":
                    "completed",

                "result":
                    result,
            }
        ), 200



    except Exception as exc:

        logger.exception(
            "Investigation orchestration failed for %s: %s",
            indicator,
            exc,
        )


        return jsonify(
            {
                "service":
                    "investigation-orchestration",

                "indicator":
                    indicator,

                "status":
                    "failed",

                "error":
                    "Investigation orchestration failed",
            }
        ), 500