from flask import Blueprint, jsonify


from app.ai.autonomous_learning_engine.learning_controller import (
    generate_learning
)



autonomous_learning_engine = Blueprint(

    "autonomous_learning_engine",

    __name__

)



@autonomous_learning_engine.route(

    "/autonomous-learning-engine/<int:user_id>",

    methods=["GET"]

)

def get_autonomous_learning_engine(user_id):


    result = generate_learning(user_id)


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_learning_engine":

            result

    })