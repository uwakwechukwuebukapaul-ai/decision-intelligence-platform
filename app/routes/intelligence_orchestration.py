from flask import Blueprint, jsonify, request

from app.ai.orchestration_engine.workflow_manager import (
    workflow_manager
)

from app.ai.orchestration_engine.intelligence_router import (
    router
)

from app.ai.orchestration_engine.decision_pipeline import (
    decision_pipeline
)


intelligence_orchestration_bp = Blueprint(

    "intelligence_orchestration",

    __name__

)



@intelligence_orchestration_bp.route(
    "/intelligence-orchestration/<int:user_id>",
    methods=["GET"]
)
def intelligence_orchestration(user_id):


    workflow = workflow_manager.create_workflow(
        user_id
    )


    completed_workflow = workflow_manager.execute_workflow(
        workflow
    )


    routing = router.route_request(
        user_id
    )


    pipeline = decision_pipeline.execute(
        user_id
    )


    return jsonify({

        "intelligence_orchestration_engine":

        {

            "status":
                "active",


            "version":
                "1.0",


            "workflow":
                completed_workflow,


            "routing":
                routing,


            "decision_pipeline":
                pipeline

        }

    })