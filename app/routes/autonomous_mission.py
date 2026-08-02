from flask import Blueprint, jsonify


from app.ai.autonomous_mission.mission_controller import (
    MissionController
)



autonomous_mission_bp = Blueprint(

    "autonomous_mission",

    __name__

)



controller = MissionController()



@autonomous_mission_bp.route(
    "/autonomous-mission/<int:user_id>",
    methods=["GET"]
)

def autonomous_mission(user_id):


    result = controller.run(

        user_id

    )


    return jsonify({


        "status":

            "operational",


        "autonomous_mission":

            result


    })