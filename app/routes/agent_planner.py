"""
AI Agent Planner API


Endpoint:


GET /agent-planner/<user_id>


Provides:

- AI execution plan
- Tool selection
- Workflow reasoning
"""


from flask import Blueprint, jsonify, request



from app.ai.agent_planner.planner_engine import (

    generate_execution_plan

)




agent_planner_bp = Blueprint(

    "agent_planner",

    __name__

)




@agent_planner_bp.route(

    "/agent-planner/<int:user_id>",

    methods=["GET"]

)

def agent_planner(user_id):


    objective = request.args.get(

        "objective",

        "Determine optimal cybersecurity career progression"

    )



    result = generate_execution_plan(

        user_id=user_id,

        objective=objective

    )



    return jsonify(

        {

            "agent_planner":

                result

        }

    )