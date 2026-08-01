from flask import Blueprint, jsonify

from app.database.db import SessionLocal

from app.models.skill_progress import SkillProgress
from app.models.user import UserProfile

from app.ai.progress.progress_engine import generate_progress


progress_bp = Blueprint(
    "progress",
    __name__
)



# =====================================
# AI Progress Intelligence Dashboard API
# =====================================

@progress_bp.route(
    "/progress/user/<int:user_id>",
    methods=["GET"]
)
def user_progress(user_id):


    db = SessionLocal()


    try:


        user = db.query(UserProfile).filter(
            UserProfile.id == user_id
        ).first()



        if not user:


            return jsonify({

                "error":
                "User not found"

            }),404





        skills = db.query(
            SkillProgress
        ).filter(

            SkillProgress.user_id == user_id

        ).all()





        completed_skills = []


        learning_skills = []



        skill_details = []




        for skill in skills:



            if skill.progress >= 100:

                completed_skills.append(
                    skill.skill_name
                )


            else:

                learning_skills.append(
                    skill.skill_name
                )





            skill_details.append({

                "skill":
                skill.skill_name,


                "level":
                skill.level,


                "progress":
                skill.progress,


                "status":
                skill.status

            })








        career = "AI Security Specialist"





        intelligence = generate_progress(

            career,

            completed_skills

        )






        return jsonify({


            "user":

            user.name,



            "career":

            career,



            "skill_summary": {


                "completed":

                completed_skills,


                "learning":

                learning_skills

            },



            "skills":

            skill_details,



            "career_readiness":

            intelligence,



            "engine":

            "AI Skill Progress Intelligence v19"


        })





    finally:


        db.close()