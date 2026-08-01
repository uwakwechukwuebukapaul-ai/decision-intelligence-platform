from flask import Blueprint, jsonify

from app.ai.career_simulation.simulation_engine import simulate_career_path


career_simulation_bp = Blueprint(
    "career_simulation",
    __name__
)



@career_simulation_bp.route(
    "/career-simulation/<int:user_id>",
    methods=["GET"]
)
def career_simulation(user_id):

    result = simulate_career_path(
        user_id
    )


    return jsonify(

        {
            "user_id": user_id,

            "career_simulation": result

        }

    )