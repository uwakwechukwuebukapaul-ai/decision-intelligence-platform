from flask import Blueprint, jsonify


from app.ai.autonomous_intelligence_orchestration_engine import (
    OrchestratorController
)



autonomous_intelligence_orchestration_engine = Blueprint(

    "autonomous_intelligence_orchestration_engine",

    __name__

)



@autonomous_intelligence_orchestration_engine.route(

    "/autonomous-intelligence-orchestration-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_intelligence_orchestration(user_id):


    controller = OrchestratorController(

        user_id

    )


    result = controller.execute_orchestration_cycle()


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "intelligence_orchestration_engine":

            result

    })