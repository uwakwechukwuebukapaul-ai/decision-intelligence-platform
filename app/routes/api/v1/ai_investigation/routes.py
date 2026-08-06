"""
Sentinel DNA - AI Investigation API Gateway
"""


from flask import Blueprint, jsonify


from app.intelligence.fusion import (
    SentinelIntelligenceEngine
)

from app.ai.reasoning import (
    ReasoningEngine
)

from app.ai.copilot import (
    CopilotEngine
)



ai_investigation_bp = Blueprint(

    "ai_investigation_api",

    __name__,

    url_prefix="/api/v1/ai"

)



intelligence_engine = (
    SentinelIntelligenceEngine()
)


reasoning_engine = (
    ReasoningEngine()
)


copilot_engine = (
    CopilotEngine()
)





@ai_investigation_bp.route(
    "/investigate/<indicator>",
    methods=["GET"]
)
def investigate(indicator):


    intelligence = (
        intelligence_engine.investigate(
            indicator
        )
    )


    reasoning = (
        reasoning_engine.reason(
            intelligence
        )
    )


    copilot = (
        copilot_engine.assist(
            intelligence
        )
    )


    return jsonify({

        "indicator":
            indicator,


        "intelligence":
            intelligence,


        "reasoning":
            reasoning,


        "copilot":
            copilot,


        "status":
            "completed",


        "service":
            "ai-investigation"

    })