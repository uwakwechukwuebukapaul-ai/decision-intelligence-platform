from flask import Blueprint, jsonify


from app.ai.autonomous_memory_engine.memory_controller import (

    MemoryController

)



autonomous_memory_engine = Blueprint(

    "autonomous_memory_engine",

    __name__

)



controller = MemoryController()



@autonomous_memory_engine.route(

    "/autonomous-memory-engine/<int:user_id>",

    methods=["GET"]

)

def get_autonomous_memory_engine(user_id):


    result = (

        controller.execute_memory_cycle(

            user_id

        )

    )


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_memory_engine":

            result

    })