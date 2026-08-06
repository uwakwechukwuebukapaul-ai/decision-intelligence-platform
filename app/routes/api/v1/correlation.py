"""
Sentinel DNA - Correlation Intelligence API

Exposes investigation relationship analysis.
"""


from flask import Blueprint, jsonify


from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)


from app.intelligence.correlation import (
    CorrelationEngine,
)




correlation_api_bp = Blueprint(
    "correlation_api",
    __name__,
)




@correlation_api_bp.route(
    "/api/v1/intelligence/ioc/<indicator>/correlation",
    methods=["GET"],
)
def correlate_ioc(indicator):


    try:


        intelligence = IntelligenceFusion().analyze(
            indicator
        )


        result = CorrelationEngine().analyze(
            intelligence
        )


        return jsonify(
            {
                "service": "correlation-intelligence",
                "indicator": indicator,
                "correlation": result,
            }
        )



    except Exception as exc:


        return jsonify(
            {
                "service": "correlation-intelligence",
                "status": "failed",
                "indicator": indicator,
                "error": str(exc),
            }
        ), 500