from flask import Blueprint, jsonify


from app.ai.autonomous_validation_engine import (
    ValidationController
)



autonomous_validation_engine = Blueprint(

    "autonomous_validation_engine",

    __name__

)



@autonomous_validation_engine.route(

    "/autonomous-validation-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_validation(user_id):


    controller = ValidationController(

        user_id

    )


    result = controller.execute_validation_cycle()



    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_validation_engine":

            result

    })