from flask import Blueprint, jsonify


from app.ai.autonomous_predictive_intelligence_engine import (
    PredictionController
)



autonomous_predictive_intelligence_engine = Blueprint(

    "autonomous_predictive_intelligence_engine",

    __name__

)



@autonomous_predictive_intelligence_engine.route(

    "/autonomous-predictive-intelligence-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_predictive_intelligence(user_id):


    controller = PredictionController(
        user_id
    )


    result = controller.execute_prediction_cycle()


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_predictive_intelligence_engine":

            result

    })