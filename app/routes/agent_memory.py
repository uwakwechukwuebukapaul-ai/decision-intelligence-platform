"""
AI Agent Memory API


Endpoint:

GET /agent-memory/<user_id>


Provides:

- Agent memory context
- Historical intelligence
- Learning patterns
"""


from flask import Blueprint, jsonify



from app.ai.agent_memory.memory_engine import (

    generate_agent_memory

)




agent_memory_bp = Blueprint(

    "agent_memory",

    __name__

)





@agent_memory_bp.route(

    "/agent-memory/<int:user_id>",

    methods=["GET"]

)

def agent_memory(user_id):


    result = generate_agent_memory(

        user_id

    )


    return jsonify(

        {


            "agent_memory":

                result,



            "memory_version":

                "1.0"


        }

    )