from flask import Blueprint, jsonify

from app.database.db import SessionLocal
from app.models import UserProfile

from app.ai.mentor.mentor_engine import generate_mentor_guidance


mentor_bp = Blueprint(
    "mentor",
    __name__
)



@mentor_bp.route(
    "/mentor/<int:user_id>",
    methods=["GET"]
)
def mentor_guidance(user_id):

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
                    "error": "User not found"
                }
            ), 404



        advice = generate_mentor_guidance(

            career=getattr(
                user,
                "goal",
                "SOC Analyst"
            ),


            skills=getattr(
                user,
                "skills",
                []
            ),


            progress=50,


            completed_labs=[],


            certifications=[]

        )


        return jsonify(

            {
                "user":
                    getattr(
                        user,
                        "name",
                        "Unknown"
                    ),


                "mentor":
                    advice

            }

        )


    finally:

        db.close()