"""
Sentinel DNA Investigation API

Creates and executes AI SOC investigations.
"""


from flask import Blueprint, request, jsonify
import uuid


from app.investigations import Investigation


from app.ai.agents import (
    AgentRegistry,
    EvidenceAgent,
    ThreatIntelligenceAgent
)


from app.ai.investigation_orchestrator import (
    InvestigationOrchestrator
)



investigation_bp = Blueprint(
    "investigation_api",
    __name__,
    url_prefix="/api/investigations"
)



# =====================================
# Agent Runtime
# =====================================

registry = AgentRegistry()


registry.register(
    EvidenceAgent()
)


registry.register(
    ThreatIntelligenceAgent()
)



orchestrator = InvestigationOrchestrator(
    registry
)



# Temporary memory storage.
# Replace with database repository.

investigations = {}



# =====================================
# Create Investigation
# =====================================

@investigation_bp.route(
    "/create",
    methods=["POST"]
)
def create_investigation():

    data = request.get_json()


    if not data:

        return jsonify(
            {
                "error": "Request body required"
            }
        ), 400



    investigation_id = (
        "INV-"
        +
        str(uuid.uuid4())[:8]
    )



    investigation = Investigation(

        investigation_id,

        data.get(
            "case_id"
        ),

        data.get(
            "evidence",
            []
        )
    )



    investigations[investigation_id] = investigation



    result = orchestrator.investigate(
        investigation
    )


    return jsonify(
        result
    ), 201



# =====================================
# Retrieve Investigation
# =====================================

@investigation_bp.route(
    "/<investigation_id>",
    methods=["GET"]
)
def get_investigation(
    investigation_id
):

    investigation = investigations.get(
        investigation_id
    )


    if not investigation:

        return jsonify(
            {
                "error":
                "Investigation not found"
            }
        ), 404



    return jsonify(
        investigation.report()
    )