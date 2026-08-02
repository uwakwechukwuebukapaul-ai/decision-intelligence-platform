from flask import Blueprint, jsonify


from app.ai.agent_governance.governance_engine import (
    GovernanceEngine
)



agent_governance_bp = Blueprint(

    "agent_governance",

    __name__

)



governance_engine = GovernanceEngine()



@agent_governance_bp.route(
    "/agent-governance/<int:user_id>",
    methods=["GET"]
)

def agent_governance(user_id):


    result = governance_engine.govern_agent_execution(

        user_id

    )


    return jsonify({


        "agent_governance":

            result,


        "status":

            "operational"


    })