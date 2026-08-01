"""
AI Decision Orchestrator API


Endpoint:

GET /decision-orchestrator/<user_id>


Provides:

- Unified intelligence pipeline
- Decision confidence
- AI recommendation
- Future career direction

"""


from flask import Blueprint, jsonify



from app.ai.decision_orchestrator.orchestrator_engine import (

    generate_decision_orchestration

)




decision_orchestrator_bp = Blueprint(

    "decision_orchestrator",

    __name__

)




@decision_orchestrator_bp.route(

    "/decision-orchestrator/<int:user_id>",

    methods=["GET"]

)

def decision_orchestrator(user_id):



    # =========================================
    # Temporary Intelligence Inputs
    # Future:
    # Load from database engines
    # =========================================


    memory_data = {


        "completed_actions":[

            "Built Home SOC Lab",

            "Analyzed phishing attacks",

            "Practiced threat hunting"

        ],


        "learning_behavior":

            "Practical laboratory learning"

    }




    graph_data = {


        "nodes": [

            "Python",

            "Threat Hunting",

            "SIEM Investigation",

            "Security Architect"

        ]

    }




    reasoning_data = {


        "recommendation":

            "Security Engineer transition",


        "confidence":

            85

    }




    simulation_data = {


        "future_role":

            "Security Engineer"

    }




    evolution_data = {


        "next_stage":

            "Advanced Security Professional"

    }




    result = generate_decision_orchestration(

        user_id=user_id,

        memory_data=memory_data,

        graph_data=graph_data,

        reasoning_data=reasoning_data,

        simulation_data=simulation_data,

        evolution_data=evolution_data

    )




    return jsonify(


        {

            "decision_orchestrator":

                result

        }


    )