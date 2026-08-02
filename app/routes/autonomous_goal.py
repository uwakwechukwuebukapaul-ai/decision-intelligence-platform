from flask import Blueprint, jsonify

from app.ai.autonomous_goal import (
    GoalGenerator,
    ObjectiveEngine,
    PriorityEngine,
    GoalMemory
)


from datetime import datetime



autonomous_goal_bp = Blueprint(

    "autonomous_goal",

    __name__

)



goal_generator = GoalGenerator()

objective_engine = ObjectiveEngine()

priority_engine = PriorityEngine()

goal_memory = GoalMemory()



@autonomous_goal_bp.route(
    "/autonomous-goal/<int:user_id>",
    methods=["GET"]
)

def autonomous_goal(user_id):


    goal = goal_generator.generate_goal(
        user_id
    )


    objectives = objective_engine.create_objectives(
        goal
    )


    priority = priority_engine.prioritize(
        goal
    )


    memory = goal_memory.store_goal(
        goal
    )



    return jsonify(


        {


            "status":
                "operational",


            "autonomous_goal":

                {


                    "user_id":
                        user_id,


                    "goal":
                        goal,


                    "objectives":
                        objectives,


                    "priority":
                        priority,


                    "memory":
                        memory,


                    "goal_status":
                        "generated",


                    "confidence":
                        99,


                    "generated_at":
                        datetime.utcnow().isoformat(),


                    "version":
                        "1.0"


                }


        }

    )