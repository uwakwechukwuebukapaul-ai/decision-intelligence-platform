from flask import Blueprint, jsonify


from app.ai.autonomous_adaptation_engine.adaptation_controller import (
    generate_adaptation
)



autonomous_adaptation_engine = Blueprint(

    "autonomous_adaptation_engine",

    __name__

)



@autonomous_adaptation_engine.route(

    "/autonomous-adaptation-engine/<int:user_id>",

    methods=["GET"]

)

def get_autonomous_adaptation_engine(user_id):


    result = generate_adaptation(user_id)


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_adaptation_engine":

            result

    })