from flask import Blueprint, jsonify


from app.ai.meta_intelligence.meta_controller import (
    MetaController
)

from app.ai.meta_intelligence.intelligence_coordinator import (
    IntelligenceCoordinator
)

from app.ai.meta_intelligence.knowledge_fusion import (
    KnowledgeFusion
)

from app.ai.meta_intelligence.strategic_reasoning import (
    StrategicReasoning
)

from app.ai.meta_intelligence.global_optimizer import (
    GlobalOptimizer
)

from app.ai.meta_intelligence.intelligence_state import (
    IntelligenceState
)



meta_intelligence_bp = Blueprint(
    "meta_intelligence",
    __name__
)




@meta_intelligence_bp.route(
    "/meta-intelligence/<int:user_id>",
    methods=["GET"]
)
def meta_intelligence(user_id):


    controller = MetaController()

    coordinator = IntelligenceCoordinator()

    fusion = KnowledgeFusion()

    reasoning = StrategicReasoning()

    optimizer = GlobalOptimizer()

    state = IntelligenceState()



    return jsonify(

        {


            "status":

                "operational",


            "user_id":

                user_id,


            "meta_intelligence":

                {


                    "controller":

                        controller.analyze(user_id),


                    "coordinator":

                        coordinator.coordinate(),


                    "knowledge_fusion":

                        fusion.fuse(),


                    "strategic_reasoning":

                        reasoning.reason(),


                    "global_optimizer":

                        optimizer.optimize(),


                    "intelligence_state":

                        state.get_state(),


                    "overall_meta_score":

                        99,


                    "version":

                        "1.0"

                }

        }

    )