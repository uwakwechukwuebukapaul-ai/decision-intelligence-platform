"""
AI Decision Memory API

Endpoint:

GET /memory/<user_id>

Provides:
- User memory profile
- Previous decisions
- Completed actions
- Future prediction
"""


from flask import Blueprint, jsonify


from app.ai.decision_memory.memory_engine import (
    generate_memory_profile
)




memory_bp = Blueprint(

    "memory",

    __name__

)



@memory_bp.route(

    "/memory/<int:user_id>",

    methods=["GET"]

)

def decision_memory(user_id):


    # ==================================
    # Future Database Integration
    # ==================================
    #
    # Later load:
    #
    # UserProfile
    # AI Reports
    # LearningProgress
    # Career History
    #
    

    result = generate_memory_profile(

        user_id=user_id,


        previous_goals=[

            "SOC Analyst",

            "Security Professional"

        ],


        completed_actions=[

            "Built Home SOC Lab",

            "Analyzed phishing attacks",

            "Practiced threat hunting"

        ],


        skill_history=[

            "Python",

            "Threat Hunting",

            "SIEM Investigation"

        ],


        learning_history={


            "learning_style":

                "Practical laboratory learning",


            "consistency":

                "Improving"


        }

    )



    return jsonify(result)