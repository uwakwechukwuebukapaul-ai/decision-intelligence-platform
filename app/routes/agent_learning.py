"""
AI Agent Learning API


Endpoint:

GET /agent-learning/<user_id>
"""


from flask import Blueprint, jsonify



from app.ai.agent_learning.learning_engine import (

    generate_agent_learning

)




agent_learning_bp = Blueprint(

    "agent_learning",

    __name__

)




@agent_learning_bp.route(

    "/agent-learning/<int:user_id>",

    methods=["GET"]

)

def agent_learning(user_id):


    result = generate_agent_learning(

        user_id

    )


    return jsonify(

        {


            "agent_learning":

                result,


            "learning_version":

                "1.0"


        }

    )