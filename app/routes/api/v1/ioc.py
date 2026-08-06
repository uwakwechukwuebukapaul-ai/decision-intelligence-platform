"""
Sentinel DNA API Gateway v1

IOC Intelligence API

Provides external access to:
- Indicator parsing
- IOC analysis
- Risk scoring
- Automated IOC investigation workflow
"""

from flask import (
    Blueprint,
    jsonify,
)


from app.intelligence.ioc.ioc_service import (
    IOCService,
)


from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)


from app.intelligence.ioc.workflow import (
    IOCCaseOrchestrator,
)



ioc_service = IOCService()


fusion_engine = IntelligenceFusion()


case_orchestrator = IOCCaseOrchestrator()



ioc_api_bp = Blueprint(
    "ioc_api",
    __name__,
    url_prefix="/api/v1/intelligence",
)



@ioc_api_bp.route(
    "/ioc/<indicator>",
    methods=[
        "GET",
    ],
)
def analyze_ioc(
    indicator: str,
):
    """
    Basic IOC intelligence analysis.
    """


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



@ioc_api_bp.route(
    "/ioc/<indicator>/investigate",
    methods=[
        "GET",
    ],
)
def investigate_ioc(
    indicator: str,
):
    """
    Execute complete IOC investigation workflow.

    Flow:

    IOC
      |
      v
    Intelligence Fusion
      |
      v
    Threat Decision
      |
      v
    Case Trigger
      |
      v
    Persistent Case Creation
    """


    intelligence = fusion_engine.analyze(
        indicator
    )


    investigation = case_orchestrator.process(
        intelligence
    )


    return jsonify(
        {
            "service": "ioc-investigation",

            "indicator": indicator,

            "investigation": investigation,
        }
    )