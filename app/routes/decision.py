from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.user import UserProfile

from app.data.careers import (
    get_career_profile
)



decision_bp = Blueprint(
    "decision",
    __name__
)



@decision_bp.route(
    "/decision/<int:user_id>",
    methods=["GET"]
)
def decision_engine(user_id):


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




        career = user.goals or "SOC Analyst"



        career_profile = get_career_profile(
            career
        )



        if not career_profile:


            career = "SOC Analyst"


            career_profile = get_career_profile(
                career
            )




        user_skills = []


        if user.skills:


            user_skills = [

                skill.strip()

                for skill in user.skills.split(",")

            ]




        required_skills = (

            career_profile[
                "required_skills"
            ]

        )




        missing_skills = [

            skill

            for skill in required_skills

            if skill not in user_skills

        ]



        matched_skills = [

            skill

            for skill in required_skills

            if skill in user_skills

        ]




        readiness = int(

            (
                len(matched_skills)

                /

                len(required_skills)

            )

            *

            100

        )





        next_actions = []



        for skill in missing_skills[:5]:


            next_actions.append({

                "skill":

                skill,


                "action":

                f"Start {skill} training"

            })





        return jsonify({



            "user":

            user.name,



            "career":

            career,



            "readiness_score":

            readiness,



            "analysis":{


                "strengths":

                matched_skills,


                "gaps":

                missing_skills


            },



            "decision":{


                "priority":

                (

                f"Improve {missing_skills[0]} first"

                if missing_skills

                else

                "Continue advanced training"

                ),



                "next_actions":

                next_actions


            },



            "career_requirements":{


                "level":

                career_profile["level"],


                "tools":

                career_profile[
                    "recommended_tools"
                ],


                "certifications":

                career_profile[
                    "certifications"
                ]

            }


        })





    finally:


        db.close()