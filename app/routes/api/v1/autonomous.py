"""
Sentinel DNA - Autonomous Investigation API

Provides external access to autonomous
IOC investigation workflows.
"""


from flask import (
    Blueprint,
    jsonify,
)


from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)


from app.autonomous_investigation import (
    AutonomousExecutor,
)



autonomous_api_bp = Blueprint(
    "autonomous_api",
    __name__,
    url_prefix="/api/v1/intelligence",
)



fusion = IntelligenceFusion()

executor = AutonomousExecutor()



@autonomous_api_bp.route(
    "/ioc/<indicator>/autonomous",
    methods=["GET"],
)
def autonomous_investigation(
    indicator: str,
):


    intelligence = fusion.analyze(
        indicator
    )


    investigation = executor.execute(
        intelligence
    )


    return jsonify(

        {

            "service":
                "autonomous-investigation",

            "indicator":
                indicator,

            "investigation":
                investigation,

        }

    )