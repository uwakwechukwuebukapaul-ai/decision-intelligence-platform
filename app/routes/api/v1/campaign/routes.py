"""
Sentinel DNA - Campaign Intelligence API Gateway

Provides:

- Threat campaign detection
- Indicator clustering
- MITRE relationship analysis
"""


from flask import Blueprint, jsonify, request


from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)


from app.intelligence.campaign import (
    CampaignEngine,
)





campaign_api_bp = Blueprint(
    "campaign_api",
    __name__,
)






@campaign_api_bp.route(
    "/api/v1/intelligence/campaign/analyze",
    methods=["POST"],
)
def analyze_campaign():


    data = request.get_json(
        silent=True
    ) or {}



    indicators = data.get(
        "indicators",
        []
    )



    if not indicators:


        return jsonify(
            {
                "service":
                "campaign-intelligence",

                "status":
                "failed",

                "error":
                "No indicators supplied",
            }
        ), 400






    fusion = IntelligenceFusion()


    intelligence_items = []



    for indicator in indicators:


        intelligence_items.append(
            fusion.analyze(
                indicator
            )
        )






    result = CampaignEngine().analyze(
        intelligence_items
    )






    return jsonify(
        {
            "service":
            "campaign-intelligence",

            "status":
            "completed",

            "result":
            result,
        }
    )