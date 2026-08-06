"""
Sentinel DNA

Analyst Workspace API Gateway

Provides analyst-ready investigation workspace data.

Capabilities:

- IOC workspace intelligence
- Incident queue
- Analyst assignment
- Incident status workflow
"""


from flask import (
    Blueprint,
    jsonify,
    request,
)


from app.intelligence.ioc.fusion import (
    IntelligenceFusion,
)


from app.analyst_workspace import (
    AnalystWorkspaceService,
)


from app.workspace import (
    AnalystWorkspace,
)



workspace_service = AnalystWorkspaceService()


analyst_workspace = AnalystWorkspace()



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





@workspace_api_bp.route(
    "/incidents",
    methods=["GET"],
)
def get_incident_queue():

    incidents = (
        analyst_workspace
        .get_incident_queue()
    )


    return jsonify(

        {

            "service":
                "incident-queue",

            "count":
                len(incidents),

            "incidents":
                incidents,

        }

    )





@workspace_api_bp.route(
    "/incidents",
    methods=["POST"],
)
def create_workspace_incident():


    data = request.get_json(
        silent=True
    ) or {}


    incident = (
        analyst_workspace
        .create_workspace_incident(
            data
        )
    )


    return jsonify(

        {

            "service":
                "workspace",

            "incident":
                incident,

        }

    ), 201





@workspace_api_bp.route(
    "/incidents/<incident_id>/assign",
    methods=["POST"],
)
def assign_incident(
    incident_id,
):


    data = request.get_json(
        silent=True
    ) or {}


    analyst = data.get(
        "analyst"
    )


    incident = (
        analyst_workspace
        .assign_incident(
            incident_id,
            analyst,
        )
    )


    return jsonify(

        {

            "incident":
                incident,

        }

    )





@workspace_api_bp.route(
    "/incidents/<incident_id>/status",
    methods=["POST"],
)
def update_incident_status(
    incident_id,
):


    data = request.get_json(
        silent=True
    ) or {}


    status = data.get(
        "status"
    )


    incident = (
        analyst_workspace
        .update_status(
            incident_id,
            status,
        )
    )


    return jsonify(

        {

            "incident":
                incident,

        }

    )