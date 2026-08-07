"""
Sentinel DNA Agent API

Provides available AI investigation agents.
"""

from flask import Blueprint, jsonify


agent_bp = Blueprint(
    "agent_api",
    __name__,
    url_prefix="/api/agents"
)


# Temporary static registry.
# Future version will load dynamically
# from AgentRegistry.

agents = [
    "EvidenceAgent",
    "ThreatIntelligenceAgent",
    "MITREAgent",
    "RiskAgent",
    "ResponseAgent"
]


@agent_bp.route(
    "",
    methods=["GET"]
)
def list_agents():
    """
    Return available AI agents.
    """

    return jsonify(
        {
            "platform": "Sentinel DNA",
            "service": "agent_registry",
            "status": "active",
            "agents": agents,
            "count": len(agents)
        }
    )