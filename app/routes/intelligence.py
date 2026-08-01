from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models import UserProfile

from app.ai.intelligence.user_intelligence import (
    build_user_intelligence
)


intelligence_bp = Blueprint(
    "intelligence",
    __name__
)



@intelligence_bp.route(
    "/intelligence/<int:user_id>",
    methods=["GET"]
)

def user_intelligence(user_id):


    db = SessionLocal()


    try:

        user = db.query(
            UserProfile
        ).filter(
            UserProfile.id == user_id
        ).first()



        if not user:

            return jsonify(
                {
                    "error":
                    "User not found"
                }
            ),404



        result = build_user_intelligence(
            user,
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


        return jsonify(result)



    finally:

        db.close()