from flask import Blueprint, jsonify


from app.ai.intelligence_memory_fabric.memory_controller import (
    MemoryController
)



intelligence_memory_fabric_bp = Blueprint(

    "intelligence_memory_fabric",

    __name__

)



controller = MemoryController()



@intelligence_memory_fabric_bp.route(
    "/intelligence-memory-fabric/<int:user_id>"
)
def intelligence_memory_fabric(user_id):


    return jsonify(

        {

            "status": "operational",

            "intelligence_memory_fabric":

                controller.generate_memory_state(user_id)

        }

    )