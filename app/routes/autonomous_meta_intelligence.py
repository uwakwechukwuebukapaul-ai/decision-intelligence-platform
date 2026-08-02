from flask import Blueprint, jsonify


from app.ai.autonomous_meta_intelligence.capability_manager import (
    CapabilityManager
)


from app.ai.autonomous_meta_intelligence.system_optimizer import (
    SystemOptimizer
)


from app.ai.autonomous_meta_intelligence.intelligence_selector import (
    IntelligenceSelector
)


from app.ai.autonomous_meta_intelligence.meta_state import (
    MetaState
)


from app.ai.autonomous_meta_intelligence.meta_feedback import (
    MetaFeedback
)



autonomous_meta_intelligence = Blueprint(

    "autonomous_meta_intelligence",

    __name__

)



capability_manager = CapabilityManager()

system_optimizer = SystemOptimizer()

intelligence_selector = IntelligenceSelector()

meta_state = MetaState()

meta_feedback = MetaFeedback()



@autonomous_meta_intelligence.route(

    "/autonomous-meta-intelligence/<int:user_id>",

    methods=["GET"]

)

def get_autonomous_meta_intelligence(user_id):


    capabilities = (

        capability_manager.evaluate_capabilities()

    )


    optimization = (

        system_optimizer.optimize_system(

            "Autonomous Intelligence Platform"

        )

    )


    intelligence = (

        intelligence_selector.select_optimal_intelligence_path(

            {

                "system_health":

                    "optimal"

            }

        )

    )


    state = meta_state.get_state()


    feedback = meta_feedback.process_feedback()



    return jsonify({


        "status":

            "operational",



        "user_id":

            user_id,



        "autonomous_meta_intelligence":

            {


                "capabilities":

                    capabilities,


                "optimization":

                    optimization,


                "intelligence_selection":

                    intelligence,


                "state":

                    state,


                "feedback":

                    feedback

            }

    })