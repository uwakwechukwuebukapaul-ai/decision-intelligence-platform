from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile

from app.ai.recommendation.recommendation_engine import (
    generate_recommendations
)



recommendation_bp = Blueprint(
    "recommendation",
    __name__
)




@recommendation_bp.route(
    "/recommendations/<int:user_id>",
    methods=["GET"]
)
def recommendations(user_id):


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

            }),404




        missing_skills = [


            "SIEM",

            "Incident Response",

            "Threat Hunting"

        ]




        result = generate_recommendations(

            "SOC Analyst",

            missing_skills

        )



        result["user"] = user.name



        return jsonify(result)




    finally:


        db.close()