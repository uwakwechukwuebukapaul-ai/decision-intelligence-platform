"""
Sentinel DNA AI Copilot API

Provides analyst assistance:
- IOC explanation
- Investigation reasoning
- Recommendations
"""


from flask import Blueprint, jsonify

from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)

from app.intelligence.copilot import (
    CopilotReasoningEngine,
)



copilot_engine = CopilotReasoningEngine()
ioc_engine = IntelligenceFusion()



copilot_api_bp = Blueprint(
    "copilot_api",
    __name__,
    url_prefix="/api/v1/copilot",
)



@copilot_api_bp.route(
    "/ioc/<indicator>",
    methods=["GET"],
)
def analyze_ioc_with_copilot(
    indicator: str,
):

    intelligence = ioc_engine.analyze(
        indicator
    )


    reasoning = copilot_engine.analyze(
        intelligence
    )


    return jsonify(
        {
            "service":
                "sentinel-dna-copilot",

            "indicator":
                indicator,

            "analysis":
                reasoning,

        }
    )