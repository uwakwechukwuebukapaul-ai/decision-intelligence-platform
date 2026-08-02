from flask import Blueprint, jsonify


from app.ai.agent_swarm.swarm_controller import (
    SwarmController
)



agent_swarm_bp = Blueprint(

    "agent_swarm",

    __name__

)



controller = SwarmController()



@agent_swarm_bp.route(

    "/agent-swarm/<int:user_id>",

    methods=["GET"]

)

def agent_swarm(user_id):


    result = controller.execute_swarm(

        user_id

    )


    return jsonify(

        {


            **result,


            "status":

                "operational"


        }

    )