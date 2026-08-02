from flask import Blueprint, jsonify


from app.ai.autonomous_meta_intelligence_engine import (
    MetaController
)



autonomous_meta_intelligence_engine = Blueprint(

    "autonomous_meta_intelligence_engine",

    __name__

)



controller = MetaController()



@autonomous_meta_intelligence_engine.route(

    "/autonomous-meta-intelligence-engine/<int:user_id>",

    methods=["GET"]

)

def autonomous_meta_intelligence(user_id):


    result = controller.execute_meta_cycle(

        user_id

    )


    return jsonify({

        "status":

            "operational",


        "user_id":

            user_id,


        "autonomous_meta_intelligence_engine":

            result

    })