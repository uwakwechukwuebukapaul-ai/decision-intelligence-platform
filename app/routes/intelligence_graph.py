"""
AI Intelligence Graph API

Endpoint:

GET /intelligence-graph/<user_id>

Provides:
- Knowledge relationship mapping
- Skill dependency graph
- Career intelligence connections
- AI reasoning foundation
"""


from flask import Blueprint, jsonify


from app.ai.intelligence_graph.graph_engine import (
    generate_intelligence_graph
)



intelligence_graph_bp = Blueprint(

    "intelligence_graph",

    __name__

)



@intelligence_graph_bp.route(

    "/intelligence-graph/<int:user_id>",

    methods=["GET"]

)

def intelligence_graph(user_id):


    skills = [

        "Python",

        "Threat Hunting",

        "SIEM Investigation"

    ]



    labs = [

        "Home SOC Lab",

        "Phishing Investigation Lab",

        "Detection Engineering Lab"

    ]



    certifications = [

        "CompTIA Security+",

        "CompTIA CySA+"

    ]



    career_goal = "Security Architect"



    result = generate_intelligence_graph(

        user_id=user_id,

        skills=skills,

        certifications=certifications,

        labs=labs,

        career_goal=career_goal

    )



    return jsonify(

        {

            "user_id": user_id,

            "graph_version": "1.0",

            "intelligence_graph": result

        }

    )