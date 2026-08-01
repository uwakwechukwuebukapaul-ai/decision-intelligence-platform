from flask import Blueprint, jsonify

from app.ai.coach.coach_engine import generate_coach_plan



coach_bp = Blueprint(
    "coach",
    __name__
)



@coach_bp.route(
    "/coach",
    methods=["GET"]
)

def cybersecurity_coach():

    result = generate_coach_plan(

        career="SOC Analyst",

        skills=[

            "Python",

            "Threat Hunting"

        ],

        progress=40,

        certifications=[

            "CompTIA Security+"

        ]

    )


    return jsonify(result)