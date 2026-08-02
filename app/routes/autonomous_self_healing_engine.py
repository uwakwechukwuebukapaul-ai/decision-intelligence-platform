from flask import Blueprint, jsonify


from app.ai.autonomous_self_healing_engine import (
    HealingController
)



autonomous_self_healing_engine = Blueprint(

    "autonomous_self_healing_engine",

    __name__

)



controller = HealingController()



@autonomous_self_healing_engine.route(

    "/autonomous-self-healing-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_self_healing(user_id):


    result = controller.execute_healing_cycle(

        user_id

    )


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_self_healing_engine":

            result

    })