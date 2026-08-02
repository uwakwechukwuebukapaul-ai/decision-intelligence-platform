from flask import Blueprint, jsonify

from app.ai.evaluation_engine.evaluator import run_evaluation


intelligence_evaluation_bp = Blueprint(

    "intelligence_evaluation",

    __name__

)



@intelligence_evaluation_bp.route(
    "/autonomous-evaluation/<int:user_id>",
    methods=["GET"]
)

def autonomous_evaluation(user_id):

    result = run_evaluation(user_id)

    return jsonify({

        "autonomous_evaluation_engine":
            result

    })