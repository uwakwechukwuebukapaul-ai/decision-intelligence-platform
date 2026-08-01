from flask import Blueprint, jsonify

from app.ai.digital_twin.digital_twin_engine import generate_digital_twin


digital_twin_bp = Blueprint(
    "digital_twin",
    __name__
)



@digital_twin_bp.route(
    "/digital-twin/<int:user_id>",
    methods=["GET"]
)
def digital_twin_profile(user_id):

    result = generate_digital_twin(
        user_id
    )

    return jsonify(result)