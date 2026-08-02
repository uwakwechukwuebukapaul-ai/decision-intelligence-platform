from flask import Blueprint, jsonify


from app.ai.autonomous_meta_intelligence_engine_v2 import (
    MetaController
)



autonomous_meta_intelligence_engine_v2 = Blueprint(

    "autonomous_meta_intelligence_engine_v2",

    __name__

)



controller = MetaController()



@autonomous_meta_intelligence_engine_v2.route(

    "/autonomous-meta-intelligence-engine-v2/<int:user_id>",

    methods=["GET"]

)

def autonomous_meta_intelligence_v2(user_id):


    result = controller.execute_meta_cycle(

        user_id

    )


    return jsonify({

        "status":

            "operational",


        "autonomous_meta_intelligence_engine_v2":

            result,


        "user_id":

            user_id

    })