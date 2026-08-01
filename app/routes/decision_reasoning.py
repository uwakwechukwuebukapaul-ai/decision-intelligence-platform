"""
AI Decision Reasoning API


Endpoint:

GET /decision-reasoning/<user_id>


Provides:

- AI reasoning chain
- Career decision explanation
- Strategic recommendations
"""


from flask import Blueprint, jsonify


from app.ai.decision_reasoning.reasoning_engine import (
    generate_decision_reasoning
)



decision_reasoning_bp = Blueprint(

    "decision_reasoning",

    __name__

)



@decision_reasoning_bp.route(

    "/decision-reasoning/<int:user_id>",

    methods=["GET"]

)

def decision_reasoning(user_id):


    current_skills = [

        "Python",

        "Threat Hunting",

        "SIEM Investigation"

    ]



    goals = [

        "SOC Analyst",

        "Security Engineer",

        "Security Architect"

    ]



    memory_state = {


        "learning_behavior":

            "Practical laboratory learning",


        "completed_actions":[

            "Built Home SOC Lab",

            "Analyzed phishing attacks",

            "Practiced threat hunting"

        ]

    }



    intelligence_graph = {


        "nodes":[

            "Python",

            "Threat Hunting",

            "SIEM Investigation",

            "Security Architect"

        ]

    }



    result = generate_decision_reasoning(

        user_id=user_id,

        current_skills=current_skills,

        goals=goals,

        memory_state=memory_state,

        intelligence_graph=intelligence_graph

    )



    return jsonify(

        {

            "reasoning_version":

                "1.0",


            "decision_reasoning":

                result

        }

    )