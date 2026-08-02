from flask import Blueprint, jsonify

from app.ai.autonomous_orchestrator.orchestrator_engine import (
    AutonomousOrchestrator
)



autonomous_orchestrator_bp = Blueprint(

    "autonomous_orchestrator",

    __name__

)



engine = AutonomousOrchestrator()



@autonomous_orchestrator_bp.route(
    "/autonomous-orchestrator/<int:user_id>",
    methods=["GET"]
)

def autonomous_orchestrator(user_id):


    result = engine.orchestrate(

        user_id

    )


    return jsonify(

        {

            "status":
                "operational",


            "autonomous_orchestrator":
                result

        }

    )