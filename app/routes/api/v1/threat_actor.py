"""
Sentinel DNA

Threat Actor Intelligence API Gateway

Provides:

- IOC threat actor correlation
- Actor confidence analysis
- MITRE technique mapping
- Investigation enrichment
"""


from flask import Blueprint, jsonify

from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)

from app.intelligence.threat_actor import (
    ThreatActorEngine,
)



threat_actor_api_bp = Blueprint(
    "threat_actor_api",
    __name__,
)



@threat_actor_api_bp.route(
    "/api/v1/intelligence/ioc/<indicator>/actors",
    methods=["GET"],
)
def analyze_threat_actor(indicator):


    intelligence = IntelligenceFusion().analyze(
        indicator
    )


    result = ThreatActorEngine().analyze(
        intelligence
    )


    return jsonify(
        {
            "service": "threat-actor-intelligence",
            "indicator": indicator,
            "result": result,
        }
    )