from flask import Blueprint, jsonify

from app.ai.intelligence_control_plane.control_controller import (
    ControlController
)


intelligence_control_plane_bp = Blueprint(

    "intelligence_control_plane",

    __name__

)


controller = ControlController()



@intelligence_control_plane_bp.route(
    "/intelligence-control-plane/<int:user_id>"
)
def intelligence_control_plane(user_id):


    return jsonify(

        {

            "status": "operational",

            "intelligence_control_plane":

                controller.generate_control_state(user_id)

        }

    )