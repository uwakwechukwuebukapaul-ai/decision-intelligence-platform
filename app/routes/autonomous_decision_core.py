from flask import Blueprint, jsonify


from app.ai.autonomous_decision_core.decision_controller import (
    generate_decision
)

from app.ai.autonomous_decision_core.action_planner import (
    create_action_plan
)

from app.ai.autonomous_decision_core.priority_engine import (
    evaluate_priority
)

from app.ai.autonomous_decision_core.execution_manager import (
    manage_execution
)

from app.ai.autonomous_decision_core.feedback_loop import (
    generate_feedback
)

from app.ai.autonomous_decision_core.decision_state import (
    get_decision_state
)



autonomous_decision_core_bp = Blueprint(

    "autonomous_decision_core",

    __name__

)



@autonomous_decision_core_bp.route(
    "/autonomous-decision-core/<int:user_id>",
    methods=["GET"]
)

def autonomous_decision_core(user_id):


    return jsonify(

        {

            "status":
                "operational",


            "user_id":
                user_id,


            "autonomous_decision_core":

                {


                    "decision_controller":

                        generate_decision(user_id),


                    "action_planner":

                        create_action_plan(user_id),


                    "priority_engine":

                        evaluate_priority(user_id),


                    "execution_manager":

                        manage_execution(user_id),


                    "feedback_loop":

                        generate_feedback(user_id),


                    "decision_state":

                        get_decision_state(user_id),


                    "overall_decision_score":
                        99,


                    "version":
                        "1.0"

                }

        }

    )