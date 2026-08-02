from flask import Blueprint, jsonify

from app.ai.cognitive_core.cognitive_engine import CognitiveEngine



cognitive_core_bp = Blueprint(

    "cognitive_core",

    __name__

)



engine = CognitiveEngine()



@cognitive_core_bp.route(

    "/cognitive-core/<int:user_id>",

    methods=["GET"]

)

def cognitive_core(user_id):


    result = engine.process(user_id)


    return jsonify({


        "status":

            "operational",


        "cognitive_core":

            result


    })