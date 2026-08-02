from flask import Blueprint, jsonify


from app.ai.autonomous_strategic_simulation_engine import (
    SimulationController
)



autonomous_strategic_simulation_engine = Blueprint(

    "autonomous_strategic_simulation_engine",

    __name__

)



@autonomous_strategic_simulation_engine.route(

    "/autonomous-strategic-simulation-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_strategic_simulation(user_id):


    controller = SimulationController(

        user_id

    )


    result = controller.execute_simulation_cycle()



    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_strategic_simulation_engine":

            result

    })