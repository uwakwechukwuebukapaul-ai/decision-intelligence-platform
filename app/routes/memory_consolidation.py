from flask import Blueprint, jsonify

from app.ai.memory_consolidation.consolidation_engine import (
    MemoryConsolidationEngine
)



memory_consolidation_bp = Blueprint(

    "memory_consolidation",

    __name__

)



engine = MemoryConsolidationEngine()



@memory_consolidation_bp.route(
    "/memory-consolidation/<int:user_id>",
    methods=["GET"]
)

def memory_consolidation(user_id):


    result = engine.consolidate(

        user_id

    )


    return jsonify(

        {

            **result,

            "status":
                "operational"

        }

    )