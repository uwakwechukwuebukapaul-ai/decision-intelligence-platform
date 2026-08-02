from flask import Blueprint, jsonify


from app.ai.autonomous_agent_workforce.workforce_controller import (
    generate_workforce
)



autonomous_agent_workforce = Blueprint(

    "autonomous_agent_workforce",

    __name__

)



@autonomous_agent_workforce.route(

    "/autonomous-agent-workforce/<int:user_id>",

    methods=["GET"]

)

def get_autonomous_agent_workforce(user_id):


    result = generate_workforce(user_id)


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_agent_workforce":

            result

    })