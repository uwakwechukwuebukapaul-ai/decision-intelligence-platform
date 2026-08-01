from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile

from app.ai.learning.learning_engine import generate_learning_plan



learning_bp = Blueprint(
    "learning",
    __name__
)



@learning_bp.route(
    "/learning-plan/<int:user_id>",
    methods=["GET"]
)

def learning_plan(user_id):


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





        plan = generate_learning_plan(

            career="SOC Analyst",

            missing_skills=missing_skills,

            level="Beginner"

        )




        plan["user"] = user.name



        return jsonify(plan)



    finally:

        db.close()