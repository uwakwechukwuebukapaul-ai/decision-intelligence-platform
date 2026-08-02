from flask import Blueprint, jsonify


from app.ai.autonomous_intelligence_learning import (
    LearningController
)



autonomous_intelligence_learning = Blueprint(
    "autonomous_intelligence_learning",
    __name__
)



@autonomous_intelligence_learning.route(
    "/autonomous-intelligence-learning/<int:user_id>",
    methods=["GET"]
)
def autonomous_intelligence_learning_route(user_id):


    controller = LearningController(
        user_id
    )


    result = controller.generate_learning_cycle()



    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_intelligence_learning":

            result

    })