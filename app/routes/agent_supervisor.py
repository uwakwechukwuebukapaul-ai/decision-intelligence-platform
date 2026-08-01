"""
AI Agent Supervisor API


Endpoint:

GET /agent-supervisor/<user_id>


Provides:

- Agent monitoring
- Workflow validation
- Execution health analysis
"""



from flask import Blueprint, jsonify



from app.ai.agent_supervisor.supervisor_engine import (

    generate_supervision_report

)




agent_supervisor_bp = Blueprint(

    "agent_supervisor",

    __name__

)





@agent_supervisor_bp.route(

    "/agent-supervisor/<int:user_id>",

    methods=["GET"]

)

def agent_supervisor(user_id):


    result = generate_supervision_report(

        user_id

    )


    return jsonify(

        {


            "agent_supervisor":

                result,



            "supervisor_version":

                "1.0"


        }

    )