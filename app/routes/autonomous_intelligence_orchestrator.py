from flask import Blueprint, jsonify


from app.ai.autonomous_intelligence_orchestrator import (
    IntelligenceOrchestrator
)



autonomous_intelligence_orchestrator = Blueprint(

    "autonomous_intelligence_orchestrator",

    __name__

)



orchestrator = IntelligenceOrchestrator()



@autonomous_intelligence_orchestrator.route(

    "/autonomous-intelligence-orchestrator/<int:user_id>",

    methods=["GET"]

)

def run_orchestrator(user_id):


    result = orchestrator.execute_cycle(

        user_id

    )


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_intelligence_orchestrator":

            result

    })