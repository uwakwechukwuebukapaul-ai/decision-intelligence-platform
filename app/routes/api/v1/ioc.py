"""
Sentinel DNA API Gateway v1

IOC Intelligence API

Provides external access to:
- Indicator parsing
- IOC analysis
- Risk scoring
"""

from flask import (
    Blueprint,
    jsonify,
)

from app.intelligence.ioc.ioc_service import (
    IOCService,
)


ioc_service = IOCService()


ioc_api_bp = Blueprint(
    "ioc_api",
    __name__,
    url_prefix="/api/v1/intelligence",
)


@ioc_api_bp.route(
    "/ioc/<indicator>",
    methods=["GET"],
)
def analyze_ioc(indicator: str):

    result = ioc_service.analyze(
        indicator
    )

    return jsonify(
        {
            "service": "ioc-intelligence",
            "indicator": indicator,
            "result": result,
        }
    )