from flask import Blueprint, jsonify


from app.ai.agent_reflection.reflection_engine import (
    ReflectionEngine
)



agent_reflection_bp = Blueprint(

    "agent_reflection",

    __name__

)



reflection_engine = ReflectionEngine()



@agent_reflection_bp.route(
    "/agent-reflection/<int:user_id>",
    methods=["GET"]
)

def agent_reflection(user_id):


    result = reflection_engine.reflect(

        user_id

    )


    return jsonify({


        "agent_reflection":

            result,


        "status":

            "operational"


    })