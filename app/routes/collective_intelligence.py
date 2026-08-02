from flask import Blueprint, jsonify


from app.ai.collective_intelligence.collective_engine import (
    CollectiveIntelligenceEngine
)



collective_intelligence_bp = Blueprint(

    "collective_intelligence",

    __name__

)



engine = CollectiveIntelligenceEngine()



@collective_intelligence_bp.route(

    "/collective-intelligence/<int:user_id>",

    methods=["GET"]

)

def collective_intelligence(user_id):


    result = engine.execute_collective_cycle(

        user_id

    )


    return jsonify(

        {


            **result,


            "status":

                "operational"


        }

    )