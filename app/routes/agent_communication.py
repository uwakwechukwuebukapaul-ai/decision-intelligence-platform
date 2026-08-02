from flask import Blueprint, jsonify

from app.ai.agent_communication.communication_engine import (
    CommunicationEngine
)



agent_communication_bp = Blueprint(

    "agent_communication",

    __name__

)



engine = CommunicationEngine()



@agent_communication_bp.route(
    "/agent-communication/<int:user_id>",
    methods=["GET"]
)

def agent_communication(user_id):


    result = engine.coordinate_agents(

        user_id

    )


    return jsonify({


        "agent_communication":

            result,


        "status":

            "operational"


    })