from flask import Blueprint, jsonify


from app.ai.simulation.career_simulator import (
    simulate_career_growth
)



simulation_bp = Blueprint(
    "simulation",
    __name__
)




@simulation_bp.route(
    "/simulation/<int:user_id>",
    methods=["GET"]
)

def career_simulation(user_id):


    result = simulate_career_growth(

        career="SOC Analyst",


        skills=[

            "Python",

            "Threat Hunting"

        ],


        progress=40,


        certifications=[

            "CompTIA Security+"

        ],


        labs=[

            "Home SOC Lab"

        ]

    )



    result["user_id"] = user_id



    return jsonify(result)