from flask import Blueprint, jsonify


from app.ai.agent_meta_learning.meta_learning_engine import (
    AgentMetaLearningEngine
)



agent_meta_learning_bp = Blueprint(

    "agent_meta_learning",

    __name__

)



engine = AgentMetaLearningEngine()



@agent_meta_learning_bp.route(

    "/agent-meta-learning/<int:user_id>",

    methods=["GET"]

)

def agent_meta_learning(user_id):


    result = engine.analyze_learning_process(

        user_id

    )


    return jsonify(

        {


            **result,


            "status":

                "operational"


        }

    )