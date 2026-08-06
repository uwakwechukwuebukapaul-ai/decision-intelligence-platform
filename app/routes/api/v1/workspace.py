"""
Sentinel DNA

Analyst Workspace API Gateway

Provides analyst-ready investigation workspace data.
"""


from flask import (
    Blueprint,
    jsonify,
)


from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)


from app.analyst_workspace import (
    AnalystWorkspaceService,
)



workspace_service = AnalystWorkspaceService()


workspace_api_bp = Blueprint(
    "workspace_api",
    __name__,
    url_prefix="/api/v1/workspace",
)



@workspace_api_bp.route(
    "/ioc/<indicator>",
    methods=["GET"],
)
def get_ioc_workspace(
    indicator: str,
):

    intelligence = IntelligenceFusion().analyze(
        indicator
    )


    workspace = workspace_service.build_workspace(
        intelligence
    )


    return jsonify(
        {
            "service":
                "analyst-workspace",

            "indicator":
                indicator,

            "workspace":
                workspace,
        }
    )