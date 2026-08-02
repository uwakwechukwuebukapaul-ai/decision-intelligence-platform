from flask import Blueprint, jsonify

from app.ai.agent_loop.loop_engine import AgentLoopEngine



agent_loop_bp = Blueprint(

    "agent_loop",

    __name__

)



engine = AgentLoopEngine()



@agent_loop_bp.route(

    "/agent-loop/<int:user_id>",

    methods=["GET"]

)

def agent_loop(user_id):


    result = engine.execute_loop(

        user_id

    )


    return jsonify(

        {


            "agent_loop": result,


            "status":

                "operational"

        }

    )