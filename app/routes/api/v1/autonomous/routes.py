"""
Sentinel DNA - Autonomous Investigation API
"""


from flask import Blueprint, jsonify


from app.intelligence.fusion import (
    SentinelIntelligenceEngine,
)


from app.intelligence.autonomous import (
    AutonomousInvestigationEngine,
)



autonomous_api_bp = Blueprint(
    "autonomous_api",
    __name__,
)



intel_engine = SentinelIntelligenceEngine()

auto_engine = AutonomousInvestigationEngine()



@autonomous_api_bp.route(
    "/api/v1/intelligence/ioc/<indicator>/autonomous",
    methods=["GET"],
)
def autonomous_investigation(indicator):


    intelligence = intel_engine.investigate(
        indicator
    )


    result = auto_engine.investigate(
        intelligence
    )


    return jsonify(

        {

            "service":
            "autonomous-investigation",

            "result":
            result

        }

    )