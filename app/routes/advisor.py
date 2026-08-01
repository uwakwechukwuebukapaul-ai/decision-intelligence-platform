from flask import Blueprint, jsonify

from app.database.db import SessionLocal
from app.models import UserProfile

from app.ai.advisor.career_advisor import generate_career_advice



# ===============================
# Blueprint
# ===============================

advisor_bp = Blueprint(
    "advisor",
    __name__
)



# ===============================
# Career Advisor API
# ===============================

@advisor_bp.route(
    "/advisor/<int:user_id>",
    methods=["GET"]
)
def career_advisor(user_id):

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



        career = "SOC Analyst"


        skills = []


        if hasattr(user, "skills"):

            skills = user.skills



        advice = generate_career_advice(
            career,
            skills
        )



        return jsonify(

            {

                "user":
                    user.name,


                "career_target":
                    career,


                "advisor":
                    advice

            }

        )


    finally:

        db.close()