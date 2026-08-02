from flask import Blueprint, jsonify


from app.ai.control_plane.controller import (
    control_plane
)



intelligence_control_plane_bp = Blueprint(

    "intelligence_control_plane",

    __name__

)



@intelligence_control_plane_bp.route(

    "/intelligence-control-plane/<int:user_id>",

    methods=["GET"]

)

def intelligence_control_plane(user_id):


    result = control_plane.execute_control_cycle(

        user_id

    )


    return jsonify({

        "control_plane":

            result

    })