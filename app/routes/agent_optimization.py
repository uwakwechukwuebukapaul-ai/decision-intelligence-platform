from flask import Blueprint, jsonify


from app.ai.agent_optimization.optimization_engine import (
    AgentOptimizationEngine
)



agent_optimization_bp = Blueprint(

    "agent_optimization",

    __name__

)



engine = AgentOptimizationEngine()



@agent_optimization_bp.route(

    "/agent-optimization/<int:user_id>",

    methods=["GET"]

)

def agent_optimization(user_id):


    result = engine.optimize(

        user_id

    )


    return jsonify(

        {


            **result,


            "status":

                "operational"


        }

    )