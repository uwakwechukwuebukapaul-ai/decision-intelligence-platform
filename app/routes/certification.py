from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile


certification_bp = Blueprint(
    "certification",
    __name__
)



@certification_bp.route(
    "/certifications/<int:user_id>",
    methods=["GET"]
)
def certification_plan(user_id):

    db = SessionLocal()

    try:

        user = db.query(
            UserProfile
        ).filter(
            UserProfile.id == user_id
        ).first()


        if not user:

            return jsonify({

                "error":
                "User not found"

            }), 404



        certifications = [

            {
                "name": "CompTIA Security+",
                "level": "Beginner",
                "priority": "High",
                "reason":
                "Builds cybersecurity foundation"
            },


            {
                "name": "Microsoft SC-200",
                "level": "Intermediate",
                "priority": "High",
                "reason":
                "Develops SOC Analyst skills"
            },


            {
                "name": "CompTIA CySA+",
                "level": "Intermediate",
                "priority": "Medium",
                "reason":
                "Improves threat detection and analysis"
            }

        ]


        return jsonify({

            "engine":
            "AI Certification Intelligence v1",


            "user":
            user.name,


            "career":
            "SOC Analyst",


            "total_certifications":
            len(certifications),


            "certifications":
            certifications

        })


    finally:

        db.close()