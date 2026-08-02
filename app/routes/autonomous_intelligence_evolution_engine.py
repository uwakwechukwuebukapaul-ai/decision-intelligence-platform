from flask import Blueprint, jsonify


from app.ai.autonomous_intelligence_evolution_engine import (
    EvolutionController
)



autonomous_intelligence_evolution_engine = Blueprint(

    "autonomous_intelligence_evolution_engine",

    __name__

)



@autonomous_intelligence_evolution_engine.route(

    "/autonomous-intelligence-evolution-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_intelligence_evolution(user_id):


    controller = EvolutionController(

        user_id

    )


    result = controller.execute_evolution_cycle()



    return jsonify({

        "status":
            "operational",


        "user_id":
            user_id,


        "autonomous_intelligence_evolution_engine":
            result

    })