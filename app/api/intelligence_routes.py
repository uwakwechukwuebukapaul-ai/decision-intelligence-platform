"""
Intelligence API Routes

Flask endpoints for Sentinel DNA investigations.
"""


from flask import (
    Blueprint,
    request,
    jsonify,
)


intelligence_bp = Blueprint(
    "intelligence",
    __name__,
)



def get_investigation_service():

    from app.intelligence.api import (
        InvestigationAPI,
    )

    from app.intelligence.orchestration import (
        InvestigationOrchestrator,
    )

    from app.intelligence.reasoning import (
        ReasoningEngine,
    )

    from app.intelligence.reporting import (
        ReportGenerator,
    )

    from app.intelligence.coordination import (
        Coordinator,
    )

    from app.intelligence.runtime.bootstrap import (
        create_intelligence_runtime,
    )


    executor = create_intelligence_runtime()


    coordinator = Coordinator(
        executor=executor
    )


    orchestrator = InvestigationOrchestrator(

        coordinator,

        ReasoningEngine(),

        ReportGenerator(),

    )


    return InvestigationAPI(
        orchestrator
    )



@intelligence_bp.route(
    "/api/investigate",
    methods=["POST"],
)
def investigate():


    data = request.get_json()


    if not data:

        return jsonify(
            {
                "error":
                    "JSON body required"
            }
        ), 400



    case_id = data.get(
        "case_id"
    )


    if not case_id:

        return jsonify(
            {
                "error":
                    "case_id required"
            }
        ), 400



    service = get_investigation_service()



    result = service.create_investigation(

        case_id,

        data.get(
            "execution_plan",
            {}
        ),

    )


    return jsonify(
        result
    )