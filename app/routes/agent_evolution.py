from flask import Blueprint, jsonify


from app.ai.agent_evolution.evolution_engine import (
    AgentEvolutionEngine
)



agent_evolution_bp = Blueprint(

    "agent_evolution",

    __name__

)



engine = AgentEvolutionEngine()



@agent_evolution_bp.route(

    "/agent-evolution/<int:user_id>",

    methods=["GET"]

)

def agent_evolution(user_id):


    result = engine.evolve(

        user_id

    )


    return jsonify(

        {


            **result,


            "status":

                "operational"


        }

    )