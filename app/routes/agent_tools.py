"""
AI Agent Tools API


Endpoint:

GET /agent-tools/<user_id>


Provides:

- Available AI tools
- Tool execution capability
- Agent extension layer
"""


from flask import Blueprint, jsonify



from app.ai.agent_tools.tool_registry import (

    get_available_tools

)



from app.ai.agent_tools.tool_executor import (

    execute_tool

)




agent_tools_bp = Blueprint(

    "agent_tools",

    __name__

)




@agent_tools_bp.route(

    "/agent-tools/<int:user_id>",

    methods=["GET"]

)

def agent_tools(user_id):


    tools = get_available_tools()



    return jsonify(

        {


            "user_id":

                user_id,


            "agent_tools_version":

                "1.0",


            "execution_layer":

                "ready",


            "available_tools":

                tools,


            "tool_count":

                len(tools)

        }

    )





@agent_tools_bp.route(

    "/agent-tools/<int:user_id>/execute/<tool_name>",

    methods=["GET"]

)

def execute_agent_tool(

    user_id,

    tool_name

):


    result = execute_tool(

        tool_name,

        user_id

    )


    return jsonify(

        {


            "agent_execution":

                result

        }

    )